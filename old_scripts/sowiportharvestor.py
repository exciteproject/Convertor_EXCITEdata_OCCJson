from urllib.request import urlopen

def showrecods_sowiport_id(sowid,fil_str):
    connection = urlopen("http://sowiportbeta.gesis.org:8080/solr/biblio/select?q=id%3A"+str(sowid)+fil_str+"&rows=1&wt=json&indent=true")
    response = connection.read()
    sowidict=eval(response)['response']['docs'][0]
    #return sowidict
    sowidict1={}
    urllink=[]
    for sowidictkey in sowidict.keys():
        if sowidictkey=="id":
            sowidict1["handler"]=sowidict["id"]
        elif sowidictkey=="issn":
            sowidict1[21]=sowidict["issn"]
        elif sowidictkey=="journal_full_txt_mv":
            sowidict1[118]=sowidict["journal_full_txt_mv"]
        elif sowidictkey=="language":
            sowidict1["language"]=sowidict["language"]
        elif sowidictkey=="norm_pagerange_str":
            sowidict1[104]=sowidict["norm_pagerange_str"]
        elif sowidictkey=="norm_publishDate_str":
            sowidict1[15]=sowidict["norm_publishDate_str"]
        elif sowidictkey=="title_full":
            sowidict1[64]=sowidict["title_full"]
        elif sowidictkey=="isbn":
            sowidict1[20]=sowidict["isbn"]
        elif sowidictkey=="person_author_txtP_mv":
            sowidict1[3]=sowidict["person_author_txtP_mv"]
        elif sowidictkey=="recordurl_str_mv":
            sowidict1[72]=sowidict["recordurl_str_mv"]
        elif sowidictkey=="recordurn_str_mv":
            sowidict1[85]=sowidict["recordurn_str_mv"]
        elif sowidictkey=="recorddoi_str_mv":
            sowidict1[137]=sowidict["recorddoi_str_mv"]
    return sowidict1


def create_filter(filter_list):
    if len(filter_list)>0:
        fil_str="&fl="
        for fil_item in filter_list:
            fil_str+=fil_item+"%2C"
        fil_str=fil_str[:-3]
    else:
        fil_str=""
    return fil_str


#filter_list=["id","issn","journal_full_txt_mv","language","norm_pagerange_str","norm_publishDate_str",
#             "title_full","isbn","person_author_txtP_mv","recordfulltext_str_mv","recordurl_str_mv",
#             "recordurn_str_mv","recorddoi_str_mv","doctype_lit_str"]

#sowidict=showrecods_sowiport_id("csa-pais-1994-0302653",create_filter(filter_list))