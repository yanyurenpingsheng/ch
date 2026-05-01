from utils.llm import call_llm

def analyze(data):
    history = "\n".join([d["input"] for d in data[-5:]])

    prompt = f"""
    以下是用户最近的行为记录：
    {history}

    请分析：
    1. 用户当前的问题
    2. 行为模式
    3. 潜在拖延原因
    """

    return call_llm(prompt)
