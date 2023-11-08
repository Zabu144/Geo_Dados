# pylint: disable=all
import streamlit as st;
import Controllers.RefGeoController as refGeoController
import CrudRefGeo.Cadastrar as Cadastrar

def alterar():
    paramId = st.experimental_get_query_params()
    if paramId == {}:

        colms = st.columns(10)
        campos = ['Loc_i', 'Status', 'Loc_x', 'Loc_y', 'Loc_z', 'Fase', 'Banco', 'Pol.', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)
            
        for item in refGeoController.readRefGeo():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
            col1.write(item.location_i)
            col2.write(item.status)
            col3.write(item.location_x)
            col4.write(item.location_y)
            col5.write(item.location_z)
            col6.write(item.fase)
            col7.write(item.banco)
            col8.write(item.poligono)
            button_space_excluir = col9.empty()
            on_click_excluir = button_space_excluir.button('Del', 'btnExcluir' + str(item.id))
            button_space_alterar = col10.empty()
            on_click_alterar = button_space_alterar.button('Edit', 'btnAlterar' + str(item.id))
            
            if on_click_excluir:
                refGeoController.deleteRefGeo(str(item.id))
                
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[str(item.id)]
                )
                st.experimental_rerun()
    else:
        on_click_voltar = st.button("←  Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun
        Cadastrar.cadastrar()  
        
        

        