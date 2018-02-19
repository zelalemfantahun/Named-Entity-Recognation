from nltk.parse.stanford import StanfordDependencyParser

path_to_jar = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/models/english-bidirectional-distsim.tagger'# import st
path_to_models_jar = '/home/zelalem/Downloads/stanford-postagger-2014-08-27/stanford-postagger.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

result = dependency_parser.raw_parse('I shot an elephant in my sleep')
dep = result.next()
list(dep.triples())