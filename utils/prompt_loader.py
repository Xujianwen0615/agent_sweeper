from utils.config_handler import prompts_config
from utils.path_tool import get_abs_path
from utils.logger_handler import logger

def load_system_prompts():
    try:
        system_prompts_path = get_abs_path(prompts_config['main_prompt_path'])
        print(system_prompts_path)
    except Exception as e:
        logger.error(f'[load_system_prompts]在yaml配置项中没有main_prompt_path')
        raise e

    try:
        return open(system_prompts_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f'[load_system_prompts]解析系统提示词出错{e}')
        raise e

def load_rag_prompts():
    try:
        rag_prompts_path = get_abs_path(prompts_config['rag_summarize_prompt_path'])
        # print(rag_prompts_path)
    except Exception as e:
        logger.error(f'[load_rag_prompts]在yaml配置项中没有rag_summarize_prompt_path')
        raise e

    try:
        return open(rag_prompts_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f'[load_rag_prompts]解析rag提示词出错{e}')
        raise e

def load_report_prompts():
    try:
        report_prompts_path = get_abs_path(prompts_config['report_prompt_path'])
        # print(report_prompts_path)
    except Exception as e:
        logger.error(f'[load_report_prompts]在yaml配置项中没有report_prompt_path')
        raise e

    try:
        return open(report_prompts_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f'[load_report_prompts]解析report报告提示词出错{e}')
        raise e

if __name__ == '__main__':
    print(load_rag_prompts())
