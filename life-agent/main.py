from agents.input_agent import save_input
from agents.analysis_agent import analyze
from agents.planning_agent import plan
from agents.action_agent import act

def main():
    print("🧠 Life Agent 已启动（输入 q 退出）\n")

    while True:
        user_input = input("你今天做了什么：")

        if user_input.lower() == "q":
            break

        data = save_input(user_input)

        analysis_result = analyze(data)
        print("\n📊 分析结果：\n", analysis_result)

        plan_result = plan(analysis_result)

        act(plan_result)

if __name__ == "__main__":
    main()
