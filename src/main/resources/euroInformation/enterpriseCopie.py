#
# Copyright 2022 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# paramètres de la tâche
# newTemplateName: nom du nouveau template
# templateToCopy: référence vers le template à copier
# folder: répertoire cible
# folderEnterprise: répertoire des templates enterprise

folderToGo = {} # objet répertoire de destination
enterpriseTemplateToCopy = {} # objet template à copier

# find the folder object
folderToGo = folderApi.find(folder,1)

# find the template object in the 'Enterprise' folder
folderToSearch = folderApi.find(folderEnterprise,1)
items = folderApi.getTemplates(folderToSearch.id)
for item in items:
    if item.title == templateToCopy:
        enterpriseTemplateToCopy = item

# create a new template in the 'Enterprise' folder
theNewTemplate = templateApi.copyTemplate(enterpriseTemplateToCopy.id, newTemplateName, u"Template Enterprise copié")

# move the new template from the 'Enterprise' fodler to the destination folder
folderApi.moveTemplate(folderToGo.id, theNewTemplate.id)
