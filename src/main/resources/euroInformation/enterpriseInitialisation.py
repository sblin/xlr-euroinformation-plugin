# Initialisation de la liste des templates
templates = []

folder = folderApi.find("Working/EI/Enterprise",1)
items = folderApi.getTemplates(folder.id)
for item in items:
    tags = item.tags
    if 'Enterprise' in tags:
        templates.append(item.title)

# Initialisation de la liste des répertoires
folders = []

def getFolderPathById(folderid):
    target=folderid
    foldername=folderApi.getFolder(target).title
    folderPath=""
    res = [i for i in range(len(target)) if target.startswith("/", i)]
    for p in res:
        if target[0:p] != "Applications":
            folderPath = "%s%s/"%(folderPath,folderApi.getFolder(target[0:p]).title)
    return folderPath + foldername

def addChilds(folderId):
    childs = folderApi.list(folderId, 0,50, 1, False)
    if len(childs) > 0:
        for c in childs:
            addChilds(c.id)
    else:
        folders.append(getFolderPathById(folderId))

items = folderApi.listRoot(0, 50, 1, False)
for item in items:
    addChilds(item.id)