import uuid

def generate_code():
    # code = str(datetime.now()).replace(' ', '-').upper()[:32]
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code