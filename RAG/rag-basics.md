## RAG Basics
RAG = Retrieval-Augmented Generation (检索增强生成)

### function
降低模型幻觉
1. R Retrieval 检索：靠向量数据库（ChromaDB/Milvus）做语义匹配
2. A Augmented 增强：把检索到的真实资料，塞进给大模型的提示词（Prompt）里
3. G Generation 生成整理、总结、生成答案


