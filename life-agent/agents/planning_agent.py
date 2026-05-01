from utils.llm import call_llm

def plan(analysis_result):
    prompt = f"""
    基于以下分析结果：
    {analysis_result}

    请制定一个明天的行动计划（具体到时间）
    """

    return call_llm(prompt)
