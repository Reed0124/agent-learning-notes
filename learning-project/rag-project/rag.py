from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_deepseek import ChatDeepSeek
import config_data as config


def print_prompt(prompt):
    """打印提示词（调试用）"""
    print("=" * 20)
    print(prompt.to_string())
    print("=" * 20)
    return prompt

class RagService(object):
    """
    RAG服务
    """
    def __init__(self):
        # 向量库服务：检索
        self.vector_service = VectorStoreService(DashScopeEmbeddings(model=config.embedding_model_name))

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "以我提供的已知参考资料为主，简洁的回答用户问题，参考资料：{context}。"),
                ("user", "用户提问: {question}"),
            ]
        )

        self.chat_model = ChatDeepSeek(model=config.chat_model_name)

        self.chain = self.get_chain()

    def format_func(self, doc_list: list[Document]) -> str:
        """将向量库的检索结果转换为字符串"""
        if not doc_list:
            return "无参考资料"

        formatted_str = ""
        for i, doc in enumerate(doc_list):
            formatted_str += f"[{i+1}] {doc.page_content}\n"

        return formatted_str

    def get_chain(self):
        """获取最终的执行链"""
        retriever = self.vector_service.get_retriever() # Return type: List[Document]
        chain = (
            {
                "question": RunnablePassthrough(),
                "context": retriever | self.format_func,
            }
            | self.prompt_template
            | RunnableLambda(print_prompt)
            | self.chat_model
            | StrOutputParser()
        )

        return chain


if __name__ == '__main__':
    rs = RagService()
    response = rs.chain.invoke("你好啊")
    print(response)
    print(type(response))