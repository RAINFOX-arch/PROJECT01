def is_duplicate(new_fact, facts):
   
    return any(f["id"] == new_fact["id"] for f in facts)