from src.database.models.types import Types
from src.database.models.keyword import keyword
import src.utils.utils as Utils


def perform_search(ocr, type, rule, type_doc):
    rules_liste = []
    count = 0

    keywords = keyword.where('type_id', type).get()
    for word in keywords:
        if (word.poid is not None and word.poid > 0):
            temp = Utils.strip_accents(word.keyword.lower())
            if (ocr.find(temp) != -1):
                rules_liste.append(temp)
                count += word.poid
                if (count >= rule):
                    return type, rules_liste
    return type_doc, rules_liste


def get_classify(ocr):
    type_doc = "inconnu"
    rules_listes = []
    types_list = Types.order_by('select_order', 'ASC').get()

    for item in types_list:
        if(item.rule is not None and item.rule > 0):
            type_doc, rules_liste = perform_search(ocr, item.id, item.rule, type_doc)
            if (type_doc != "inconnu"):
                rules_listes = rules_liste
                break

    return type_doc, rules_listes


def classify(base_64=None):
    results = []
    rules_listes = []
    mime_type = Utils.detect_mime_type(base_64)
    if (mime_type == "application/pdf"):
        imgs_64 = Utils.pdf_from_base64_to_images_base64(base_64)
        for img_64 in imgs_64:
            ocr = Utils.strip_accents(Utils.ocr(img_64).lower())
            type_doc, rules_liste = get_classify(ocr)
            results.append(type_doc)
            rules_listes.append(rules_liste)
    elif (mime_type):
        ocr = Utils.strip_accents(Utils.ocr(Utils.from_base64_to_base64_dpi(base_64)).lower())
        type_doc, rules_liste = get_classify(ocr)
        results.append(type_doc)
        rules_listes.append(rules_liste)
    return results, rules_listes
