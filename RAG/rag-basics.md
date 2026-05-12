## RAG Basics
RAG = Retrieval-Augmented Generation (检索增强生成)

### function
降低模型幻觉
1、R Retrieval 检索：靠向量数据库（ChromaDB/Milvus）做语义匹配<br>
2、A Augmented 增强：把检索到的真实资料，塞进给大模型的提示词（Prompt）里<br>
3、G Generation 生成整理、总结、生成答案<br>

### process
1、文档 → 嵌入模型 → 文档向量<br>
2、用户问题 → 嵌入模型 → 问题向量<br>
3、**余弦相似度算法** → 找出最像的文档<br>
4、丢给大模型回答


