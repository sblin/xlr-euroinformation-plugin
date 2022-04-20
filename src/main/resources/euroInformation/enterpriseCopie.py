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
