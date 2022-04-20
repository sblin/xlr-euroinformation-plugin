#
# Copyright 2022 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

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