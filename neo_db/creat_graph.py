from py2neo import Graph, Node, Relationship, NodeMatcher
# NodeSelector,
from config import graph

with open(r"D:\KGQA\KGQA_HLM-master\raw_data\test2.txt", encoding="UTF-8") as f:
    # 读取test文件夹中的每一行
    for line in f.readlines():
        rela_array = line.strip("\n").split(",")
        print(rela_array)
        # 构建原告类型、被告类型、所犯罪名类型节点
        graph.run("MERGE(p: Plaintiff{Name: '%s'})" % (rela_array[0]))
        graph.run("MERGE(p: Defendant{Name: '%s'})" % (rela_array[2]))
        graph.run("MERGE(p: Charge{Name: '%s'})" % (rela_array[4]))
        # 构建 原告和被告间诉讼关系，被告和罪名间犯罪关系
        graph.run(
            "MATCH (e: Defendant), (cc: Charge) \
             WHERE e.Name='%s' AND cc.Name='%s' \
             CREATE(e)-[r:%s{relation: '%s'}]->(cc) \
             RETURN r" % (rela_array[2], rela_array[4], rela_array[3], rela_array[3])
        )
        graph.run(
            "MATCH (e: Plaintiff), (cc: Defendant) \
             WHERE e.Name='%s' AND cc.Name='%s' \
             CREATE(e)-[r:%s{relation: '%s'}]->(cc) \
             RETURN r" % (rela_array[0], rela_array[2], rela_array[1], rela_array[1])
        )



    ''' 原来的代码
    for line in f.readlines():
        rela_array = line.strip("\n").split(",")
        print(rela_array)
        graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})" % (rela_array[3], rela_array[0]))
        graph.run("MERGE(p: Person{cate:'%s',Name: '%s'})" % (rela_array[4], rela_array[1]))
        graph.run(
            "MATCH(e: Person), (cc: Person) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (rela_array[0], rela_array[1], rela_array[2], rela_array[2])

        )
    '''
        
