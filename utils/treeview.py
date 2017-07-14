# class TreeNode():
#     def __init__(self):
#         self.id = "0"
#         self.text = "Node 1"
#         self.href = "#node-1"
#         self.selectable = True
#         self.state = {
#                          'checked': True,
#                          'disabled': True,
#                          'expanded': True,
#                          'selected': True,
#                      },
# #         self.tags = ['available'],
#         self.nodes = []
#     def to_dict(self):
#         icon = (len(self.nodes) > 0) and 'glyphicon glyphicon-list-alt' or 'glyphicon glyphicon-user'
#         return {
#                   'id': self.id,
#                   'text': self.text,
#                   'icon': icon,
#                   'href': self.href,
#                   'tags':  [str(len(self.nodes))],
#                   'nodes': self.nodes,
#               }

# def get_dept_tree(parents):
#     '''
#     根据提供的父节点，迭代出所有的子节点，并用一个dict的列表来表示
#     :param parents 父节点列表:
#     :return 返回dict列表:
#     '''
#     display_tree = []
#     for p in parents:
#         node = TreeNode()
#         #node.id = p.name
#         node.text = p.name
#         try:
#             children = p.children.all()
#         except:
#             host_account = p.host.count()
#             node_dict = node.to_dict()
#             node_dict["tags"] = [host_account]
#             display_tree.append(node_dict)
#             return display_tree
#         if len(children) > 0:
#             node.nodes = get_dept_tree(children)
#         display_tree.append(node.to_dict())
#     return display_tree



class TreeNode(dict):
    def __init__(self):
        self.id = "0"
        self.text = "Node1"
        self.href = "#node-1"
        self.selectable = True
        self.state = {
                        'checked': True,
#                         'disabled': True,
                        'expanded': True,
#                         'selected': True,
                     }
        self.tags = ["0"]
        self.nodes = []

        def __getattr__(self,key):
            return self[key]

        def __setattr__(self, key, value):
            self[key] = value


def get_project_tree(parent):
    '''
    根据提供的父节点，迭代出所有的子节点，并用一个dict的列表来表示
    :param parents 父节点列表:
    :return 返回dict列表:
    '''
    display_tree=[]
    for p in parent:
        node=TreeNode()
        node.text = p.__str__()
        node.nodetype = p.__class__.__name__
        node.pk = p.pk
        try:
            children=p.children.all()
            if children:
                node.nodes=get_project_tree(children)
                node.tags = [str(len(children))]
        except:
            host_account = p.host.count()
            node.tags = [host_account]

        node.icon = (len(node.nodes) > 0) and 'glyphicon glyphicon-list-alt' or 'glyphicon glyphicon-user'
        
        display_tree.append(node.__dict__)
    return display_tree
            