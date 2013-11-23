# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# - call exposes all registered services (none by default)
#

@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    if not session.auth:
        response.title = None
    #response.flash = T("Página de gestión del Banco de Alimentos de Badajoz")

    # Temporal, para importar datos de bb.dd. anterior ###
    import importacion
    # importacion.rellena_familias()
    # importacion.rellena_subfamilias()
    # importacion.rellena_alimentos()
    # importacion.rellena_paises()
    # importacion.rellena_provincias()
    # importacion.rellena_localidades()
    # importacion.rellena_colaboradores()
    #importacion.rellena_beneficiarios()
    #importacion.rellena_estanterias()
    #importacion.rellena_cabecerasalmacen()
    #importacion.rellena_lineasalmacen()
    #importacion.rellena_cabecerasentradas()
    #importacion.rellena_lineasentradas()
    #importacion.rellena_cabecerasalidas()
    #importacion.rellena_lineasalidas()
    #importacion.rellena_alimentos2()
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
