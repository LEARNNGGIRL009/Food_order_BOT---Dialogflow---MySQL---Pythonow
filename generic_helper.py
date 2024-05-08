
import re
def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""


def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


if __name__=="__main__":
    print(get_str_from_food_dict({"samosa":4,"dosa":2}) )
    #print(extract_session_id("projects/daflow-b9v9/agent/sessions/a610c5c7-d5a5-64b4-94ad-9082ef5b042d/contexts/ongoing-order") )