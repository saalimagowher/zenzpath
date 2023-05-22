import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
from streamlit_option_menu import option_menu
st.set_page_config(
    page_title ="Zen_Z_Path",
    page_icon ="chart_with_upwards_trend",
    layout = "wide"
)
df = pd.read_csv(r'C:\Users\Hp\Downloads\Colleges_WithCourseDetails_V2.0.csv')
st.markdown("<h2 style='text-align: center; color: steelblue;'>Zen_Z_Path</h2>", unsafe_allow_html=True)
st.write("Please Check this out https://zenzpath.com/Dashboard")

df.rename(columns={'Name': 'Count'},inplace = True)

with st.sidebar:
    select = option_menu(
                    menu_title=None,
                    options=["Home", "Options"],
                    icons=["house", "check"],  
                    )
if select == 'Home':
    
    image = Image.open('ZenZPath.png')
    st.subheader("Welcome to Zen-Z-Path !")
    col1, col2, col3 = st.columns(3) 
    with col1: 
        st.write(' ') 
    with col2: 
        st.image(image,width=400) 
    with col3: 
        st.write(' ')

    st.write("<span style='font-size:18px;'>Our goal is to help students make informed decisions about their academic future and provide them with guidance as they navigate the process of selecting and applying for higher education programs.</span>", unsafe_allow_html=True)
    st.write("<span style='font-size:18px;'>We understand that the transition from high school to higher education can be challenging, and our app is designed to make the process easier. Our team of experts has curated a comprehensive database of information about various higher education programs, including undergraduate, graduate programs.</span>", unsafe_allow_html=True)
    st.write("<span style='font-size:18px;'>Our app is user-friendly and provides a personalized experience to each user. You can explore higher education options that align with your interests, career goals, and educational background.</span>", unsafe_allow_html=True)
    st.write("<span style='font-size:18px;'>We are committed to keeping our app up-to-date with the latest trends and changes in higher education. We also welcome feedback from our users, as it helps us improve our app and better serve the needs of our users.</span>", unsafe_allow_html=True)
    st.write("<span style='font-size:18px;'>Thank you for choosing Zen-Z-Path App. We look forward to helping you make informed decisions and achieve your academic goals!</span>", unsafe_allow_html=True)

    
else:
    with st.sidebar.expander("Zone"):
        container = st.container()
        Zone_all = st.checkbox("Select all", key="Zone")

        if Zone_all:
            df_Zone = container.multiselect(
                "Please Select the Zone:",
                options=df["Zone"].unique(),
                default=df["Zone"].unique()
            )
        else:
            df_Zone = container.multiselect(
                "Please Select the Zone:",
                options=df["Zone"].unique()
            )
    with st.sidebar.expander("District"):
        container = st.container()
        District_all = st.checkbox("Select all", key="District")


         # Filter the districts based on the selected zones
        if not df_Zone    :
                available_districts = df["District"].unique() 
        else:
                available_districts = df[df["Zone"].isin(df_Zone)]["District"].unique() 

        if District_all:
            df_District = container.multiselect(
                "Please Select the District:",
                options=available_districts,
                default=available_districts
            )
        else:
            df_District = container.multiselect(
                "Please Select the District:",
                options=available_districts
            )
    
    #Type
    with st.sidebar.expander("Type"):
        container = st.container()
        Type_all = st.checkbox("Select all", key="Type")


        if df_Zone and df_District:
              available_Type = df[(df["Zone"].isin(df_Zone)) & (df["District"].isin(df_District))]["Type"].unique()    
        elif df_Zone and not df_District:
              available_Type = df[df["Zone"].isin(df_Zone)]["Type"].unique()                                            

        elif not df_Zone and df_District: 
             available_Type = df[df["District"].isin(df_District)]["Type"].unique()

        elif not df_Zone:
              available_Type = df["Type"].unique()                                            

        else:
            df

        if Type_all:
            df_Type = container.multiselect(
                "Please Select the Type:",
                options=available_Type,  
                default=available_Type

                )

        else:
            df_Type = container.multiselect(
                "Please Select the Type:",
                options=available_Type,  

                )



    #Stream
    with st.sidebar.expander("Stream"):
        container = st.container()
        Stream_all = st.checkbox("Select all", key="Stream")


        if df_Zone and df_District and df_Type:
            available_Stream = df[(df["Zone"].isin(df_Zone)) & (df["District"].isin(df_District))  & (df["Type"].isin(df_Type))]["Stream"].unique() 
        elif df_Zone and not df_District and not df_Type:
            available_Stream = df[df["Zone"].isin(df_Zone)]["Stream"].unique()   
        elif not df_Zone and df_District and df_Type: 
            available_Stream = df[(df["District"].isin(df_District))  & (df["Type"].isin(df_Type))]["Stream"].unique()       
        elif df_Zone and  not df_District and df_Type: 
            available_Stream = df[(df["Zone"].isin(df_Zone))  & (df["Type"].isin(df_Type))]["Stream"].unique()         
        elif not df_Zone and  not df_District and df_Type: 
            available_Stream = df[(df["Type"].isin(df_Type))]["Stream"].unique()  
        elif df_Zone and df_District and not df_Type:
            available_Stream = df[(df["Zone"].isin(df_Zone)) & (df["District"].isin(df_District))]["Stream"].unique()                        

        else:
            available_Stream = df["Stream"].unique()

        #available_Stream = df_t["Stream"].unique() 
        if Stream_all:
            df_Stream = container.multiselect(
                "Please Select the Stream:",
                options=available_Stream,
                default=available_Stream
            )
        else:
            df_Stream = container.multiselect(
                "Please Select the Stream:",
                options=available_Stream
            )
    #Branch      
    with st.sidebar.expander("Branch"):
        container = st.container()
        Branch_all = st.checkbox("Select all", key="Branch")


        if df_Zone and df_District and df_Type and df_Stream:
            available_Branch = df[(df["Zone"].isin(df_Zone)) & (df["District"].isin(df_District)) & (df["Type"].isin(df_Type)) & (df["Stream"].isin(df_Stream))]["Branch"].unique() 
        elif df_Zone and not df_District and not df_Type and not df_Stream:
            available_Branch = df[df["Zone"].isin(df_Zone)]["Branch"].unique()   
        elif not df_Zone and df_District and df_Type and df_Stream: 
            available_Branch = df[(df["District"].isin(df_District)) & (df["Type"].isin(df_Type)) & (df["Stream"].isin(df_Stream))]["Branch"].unique()       
        elif df_Zone and  not df_District and df_Type and df_Stream: 
            available_Branch = df[(df["Zone"].isin(df_Zone)) & (df["Type"].isin(df_Type)) & (df["Stream"].isin(df_Stream))]["Branch"].unique()         
        elif not df_Zone and  not df_District and not df_Type and df_Stream: 
            available_Branch = df[(df["Stream"].isin(df_Stream))]["Branch"].unique()  
        elif df_Zone and df_District and not df_Type and df_Stream:
            available_Branch = df[(df["Zone"].isin(df_Zone)) & (df["District"].isin(df_District)) & (df["Stream"].isin(df_Stream))]["Branch"].unique()   
        elif df_Zone and df_District and not df_Type and not df_Stream:
            available_Branch = df[(df["Zone"].isin(df_Zone)) & (df["District"].isin(df_District))]["Branch"].unique()
        elif df_Zone and df_District and df_Type and not df_Stream:
            available_Branch = df[(df["Zone"].isin(df_Zone)) & (df["District"].isin(df_District)) & (df["Type"].isin(df_Type))]["Branch"].unique()                     

        else:
            available_Branch = df["Branch"].unique()

        #available_Branch = df_s["Branch"].unique()
        if Branch_all:
            df_Branch = container.multiselect(
                "Please Select the Branch:",
                options=available_Branch,
                default=available_Branch
            )
        else:
            df_Branch = container.multiselect(
                "Please Select the Branch:",
                options=available_Branch
              )

    #_______________multivariate(5 variables)__________________       
    if ((df_Zone and df_District) and (df_Type and df_Stream) and df_Branch):
        st.subheader("Distribution of Zone, District, Type, Stream & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District)) & (df['Type'].isin(df_Type)) & (df['Stream'].isin(df_Stream)) & (df['Branch'].isin(df_Branch)) 
        data = df[filter]
        grouped = data.groupby(['Zone','District', 'Type', 'Stream', 'Branch'])['Count'].nunique().reset_index()
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    #_______________multivariate(4 variables)__________________       
    elif (df_Zone and df_District) and (df_Type and df_Stream):
        st.subheader("Distribution of Zone, District, Type & Stream")
        filter =(df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District)) & (df['Type'].isin(df_Type)) & (df['Stream'].isin(df_Stream))
        data = df[filter]
        grouped = data.groupby(['Zone', 'District', 'Type', 'Stream'])['Count'].nunique().reset_index()
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif (df_Zone and df_District) and (df_Stream and df_Branch):
        st.subheader("Distribution of Zone, District, Stream & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District)) & (df['Stream'].isin(df_Stream)) & (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Zone', 'District', 'Stream', 'Branch'])['Count'].nunique().reset_index()
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif (df_Zone and df_Type) and (df_Stream and df_Branch):
        st.subheader("Distribution of Zone, Type, Stream & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['Type'].isin(df_Type)) & (df['Stream'].isin(df_Stream)) & (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Zone', 'Type', 'Stream', 'Branch'])['Count'].nunique().reset_index()
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)

    elif ((df_Zone and df_District) and (df_Type and df_Branch)):
        st.subheader("Distribution of Zone, District, Type & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District)) & (df['Type'].isin(df_Type)) & (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Zone', 'District', 'Type', 'Branch'])['Count'].nunique().reset_index()
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Stream and df_District) and (df_Type and df_Branch)):
        st.subheader("Distribution of Stream, District, Type & Branch")
        filter = (df['Stream'].isin(df_Stream)) & (df['District'].isin(df_District)) & (df['Type'].isin(df_Type)) & (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Stream', 'District', 'Type', 'Branch'])['Count'].nunique().reset_index()
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    #__________multivariate(3 variables)_________________    
    elif ((df_Zone and df_District) and df_Type):
        st.subheader("Distribution of Zone, District & Type")
        filter = (df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District)) &  (df['Type'].isin(df_Type))
        data = df[filter]
        grouped = data.groupby(['Zone', 'District', 'Type'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Zone', y='Count', color='District', barmode='group', facet_col='Type', text_auto=True)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)

    elif ((df_Zone and df_Type) and df_Stream):
        st.subheader("Distribution of Zone, Type & Stream")
        filter = (df['Zone'].isin(df_Zone)) & (df['Type'].isin(df_Type)) &  (df['Stream'].isin(df_Stream))
        data = df[filter]
        grouped = data.groupby(['Zone', 'Type', 'Stream'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Zone', y='Count', color='Type', barmode='group', facet_col='Stream', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Zone and df_District) and df_Stream):
        st.subheader("Distribution of Zone, District & Stream")
        filter = (df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District)) &  (df['Stream'].isin(df_Stream))
        data = df[filter]
        grouped = data.groupby(['Zone', 'District', 'Stream'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Zone', y='Count', color='District', barmode='group', facet_col='Stream', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_District and df_Stream) and df_Branch):
        st.subheader("Distribution of District, Stream & Branch")
        filter = (df['District'].isin(df_District)) & (df['Stream'].isin(df_Stream)) &  (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['District', 'Stream', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='District', y='Count', color='Stream', barmode='group', facet_col='Branch', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Type and df_District) and df_Stream):
        st.subheader("Distribution of Type, District & Stream")
        filter = (df['Type'].isin(df_Type)) & (df['District'].isin(df_District)) &  (df['Stream'].isin(df_Stream))
        data = df[filter]
        grouped = data.groupby(['Type', 'District', 'Stream'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Type', y='Count', color='District', barmode='group', facet_col='Stream', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Type and df_District) and df_Branch):
        st.subheader("Distribution of Type, District & Branch")
        filter = (df['Type'].isin(df_Type)) & (df['District'].isin(df_District)) &  (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Type', 'District', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Type', y='Count', color='District', barmode='group', facet_col='Branch', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Type and df_Stream) and df_Branch):
        st.subheader("Distribution of Type, Stream & Branch")
        filter = (df['Type'].isin(df_Type)) & (df['Stream'].isin(df_Stream)) &  (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Type', 'Stream', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Type', y='Count', color='Stream', barmode='group', facet_col='Branch', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Zone and df_District) and df_Branch):
        st.subheader("Distribution of Zone, District & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District)) &  (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Zone', 'District', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Zone', y='Count', color='District', barmode='group', facet_col='Branch', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Zone and df_Stream) and df_Branch):
        st.subheader("Distribution of Zone, Stream & Branch")
        st.header("Distribution of Zone, Stream & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['Stream'].isin(df_Stream)) &  (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Zone', 'Stream', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Zone', y='Count', color='Stream', barmode='group', facet_col='Branch', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif ((df_Zone and df_Type) and df_Branch):
        st.subheader("Distribution of Zone, Type & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['Type'].isin(df_Type)) &  (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby(['Zone', 'Type', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Zone', y='Count', color='Type', barmode='group', facet_col='Branch', text_auto=True)
        fig.update_traces(textfont_size=14)
        fig.update_layout(legend=dict(orientation='h'))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    #_____________bivariate(district)_____________
    elif (df_District and df_Type):
        st.subheader("Distribution of District & Type")
        filter = (df['District'].isin(df_District)) & (df['Type'].isin(df_Type))  
        data = df[filter]
        grouped = data.groupby(['District', 'Type'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='District', y='Count', color='Type', barmode='group', text_auto=True) 
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif (df_District and df_Stream):
        st.subheader("Distribution of District & Stream")
        filter = (df['District'].isin(df_District)) & (df['Stream'].isin(df_Stream))  
        data = df[filter]
        grouped = data.groupby(['District', 'Stream'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='District', y='Count', color='Stream', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif (df_District and df_Branch):
        st.subheader("Distribution of District & Branch")
        filter = (df['District'].isin(df_District)) & (df['Branch'].isin(df_Branch))  
        data = df[filter]
        grouped = data.groupby(['District', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='District', y='Count', color='Branch', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    ###===========bivariate (Type)==================================================
    elif (df_Type and df_Stream):
        st.subheader("Distribution of Type & Stream")
        filter = (df['Type'].isin(df_Type)) & (df['Stream'].isin(df_Stream))  
        data = df[filter]
        grouped = data.groupby(['Type', 'Stream'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Type', y='Count', color='Stream', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif (df_Type and df_Branch):
        st.subheader("Distribution of Type & Branch")
        filter = (df['Type'].isin(df_Type)) & (df['Branch'].isin(df_Branch))  
        data = df[filter]
        grouped = data.groupby(['Type', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Type', y='Count', color='Branch', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    ###==========================bivariate(Stream)===================================
    elif (df_Stream and df_Branch):
        st.subheader("Distribution of Stream & Branch")
        filter = (df['Stream'].isin(df_Stream)) & (df['Branch'].isin(df_Branch))  
        data = df[filter]
        grouped = data.groupby(['Stream', 'Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Stream', y='Count', color='Branch', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)    
    #_____________bivariatre(Zone)___________________
    elif (df_Zone and df_District ):
        st.subheader("Distribution of Zone & District")
        filter = (df['Zone'].isin(df_Zone)) & (df['District'].isin(df_District))  
        data = df[filter]
        grouped = data.groupby(['Zone','District'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='District', y='Count', color='Zone', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif (df_Zone and df_Type):
        st.subheader("Distribution of Zone & Type")
        filter = (df['Zone'].isin(df_Zone)) & (df['Type'].isin(df_Type))   
        data = df[filter]
        grouped = data.groupby(['Zone','Type'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Type', y='Count', color='Zone', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif (df_Zone and df_Stream):
        st.subheader("Distribution of Zone & Stream")
        filter = (df['Zone'].isin(df_Zone)) & (df['Stream'].isin(df_Stream))  
        data = df[filter]
        grouped = data.groupby(['Zone','Stream'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Stream', y='Count', color='Zone', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)

    elif (df_Zone and df_Branch):
        st.subheader("Distribution of Zone & Branch")
        filter = (df['Zone'].isin(df_Zone)) & (df['Branch'].isin(df_Branch))  
        data = df[filter]
        grouped = data.groupby(['Zone','Branch'])['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Branch', y='Count', color='Zone', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    #_______________univariate_____________        

    
    elif df_Zone:
        st.subheader("Distribution of Zone")
        filter = (df['Zone'].isin(df_Zone))
        data = df[filter]
        grouped = data.groupby('Zone')['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Zone', y='Count', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
        
    elif df_District :
        st.subheader("Distribution of District")
        filter = (df['District'].isin(df_District))
        data = df[filter]
        grouped = data.groupby('District')['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='District', y='Count', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif df_Type:
        st.subheader("Distribution of Type")
        filter = (df['Type'].isin(df_Type))
        data = df[filter]
        grouped = data.groupby('Type')['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Type', y='Count', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif df_Stream:
        st.subheader("Distribution of Stream")
        filter = (df['Stream'].isin(df_Stream))
        data = df[filter]
        grouped = data.groupby('Stream')['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Stream', y='Count', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    elif df_Branch:
        st.subheader("Distribution of Branch")
        filter = (df['Branch'].isin(df_Branch))
        data = df[filter]
        grouped = data.groupby('Branch')['Count'].nunique().reset_index()
        fig = px.bar(grouped, x='Branch', y='Count', barmode='group', text_auto=True)
        fig.update_layout(legend=dict(orientation='h', yanchor='top', y=1.1))
        st.plotly_chart(fig,use_container_width=True)
        fig.update_traces(textfont_size=18)
        st.markdown(grouped.style.hide_index().to_html(), unsafe_allow_html=True)
    else:

        image = Image.open('ZenZPath.png')
        col1, col2, col3 = st.columns(3) 
        with col1: 
            st.write(' ') 
        with col2: 
            st.image(image,width=400) 
        with col3: 
            st.write(' ')

