import json


def load_candidates_from_json(): # возвращает список всех кандидатов
    with open("candidates.json", encoding='utf-8') as file:
        json_list = file.read()
        candidates_list = list(json.loads(json_list))
        return candidates_list


def get_by_id(uid): # возвращает одного кандидата по его id
    candidates_list = load_candidates_from_json()
    for item in candidates_list:
        if uid == item["id"]:
            candidate = item
            break
        else:
            continue
    return candidate


def get_candidates_by_name(candidate_name): # возвращает кандидатов по имени
    candidates_list = load_candidates_from_json()
    candidate_by_name = []
    for item in candidates_list:
        if candidate_name in item["name"]:
            candidate_by_name.append({"id":item["id"], "name":item["name"]})

    return candidate_by_name


def get_candidates_by_skill(skill_name): # возвращает кандидатов по навыкуpa
    candidates_list = load_candidates_from_json()
    candidate_by_skill = []
    for item in candidates_list:
        if skill_name in item["skills"]:
            candidate_by_skill.append({"id": item["id"], "name": item["name"]})
    print(candidate_by_skill)
    return candidate_by_skill

