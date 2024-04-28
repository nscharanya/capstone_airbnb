import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Streamlit part

st.set_page_config(layout= "wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")

def datafr():
    df= pd.read_csv("C:/Users/saich/OneDrive/Desktop/airbnb/Airbnb.csv")
    return df

df= datafr()

with st.sidebar:
    st.title("Main Menu")
    select = st.selectbox("Select Option", ["Home \U0001F3E0", "Insights & Analysis \U0001F4CA", "Project Overview \U0001F310"])

# Home
if select == "Home \U0001F3E0":
    st.markdown("## Welcome to our Airbnb project! ✈️ \U0001F3E8 ")
    st.markdown("#### \U0001F3E1 This is home tab!  Here you can find information about Airbnb.")
    st.write("")
    st.write("")
    st.markdown("## Key Features \U0001F4CB")
    st.write("")
    st.write("")
    
    col1, col2 = st.columns([4,2])
    with col1:
        
        st.write("1. Search and discover unique stays \U0001F30D")
        st.write("2. Book accommodations for your travel needs \U0001F306")
        st.write("3. Connect with hosts and explore local cultures \U0001F91D")
    with col2:
        logo_image1 = Image.open("C:/Users/saich/OneDrive/Desktop/airbnb/Couleur-logo-Airbnb.jpg")
        st.image(logo_image1, width = 350)
    
    st.write("")
    st.write("")
    st.markdown("## Why Choose Airbnb? \U0001F680")
    st.write("")
    st.write("")

    col1, col2 = st.columns([4,2])
    with col1:
        st.write("1. Diversity of accommodations, from apartments to villas \U0001F3E2")
        st.write("2. Authentic experiences with local hosts \U00002B50")
        st.write("3. Flexible booking options and secure payments \U0001F4B3")
    with col2:
        logo_image2 = Image.open("C:/Users/saich/OneDrive/Desktop/airbnb/th.jpg")
        st.image(logo_image2, width = 350)
    st.write("")
    st.write("")
    st.markdown("## Why Choose Airbnb? \U0001F680")
    st.write("")
    st.write("")

    col1, col2 = st.columns([4,2])
    with col1:
        st.write("1. Diversity of accommodations, from apartments to villas \U0001F306 \U0000FE0F")
        st.write("2. Authentic experiences with local hosts \U00002B50 \U0001F334")
        st.write("3. Flexible booking options and secure payments \U0001F4B8")
    with col2:
        airbnb_image= Image.open("C:/Users/saich/OneDrive/Desktop/airbnb/th (1).jpg")
        st.image(airbnb_image, width= 350)

    
    st.write("")
    st.write("")
    st.markdown("## Get Started with your Airbnb Journey  \U00002728")

# Charts and Visualizations
elif select == "Insights & Analysis \U0001F4CA":
    with st.sidebar:
        option = st.radio("Options to Explore",["Cost Evaluation \U0001F4B0", "Resource Assessment \U0001F4BB", "Location Based \U0001F5FA", "Map-based Analysis \U0001F310", "Top Trends \U0001F4C8"])
    if option == "Cost Evaluation \U0001F4B0":
        st.markdown("### COST EVALUATION ")

        # Filtering based on Country
        country= st.selectbox("Select the Country",df["country"].unique())

        df1= df[df["country"] == country]
        df1.reset_index(drop= True, inplace= True)

        # Filtering based on room_type
        room_type= st.selectbox("Select the Room Type",df1["room_type"].unique())
        
        df2= df1[df1["room_type"] == room_type]
        df2.reset_index(drop= True, inplace= True)
        
        df_grby= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
        df_grby.reset_index(inplace= True)

        fig_bar= px.bar(df_grby, x='property_type', y= "price", title= "TOTAL PRICE FOR PROPERTY_TYPES",
                        hover_data=["number_of_reviews","review_scores"],
                        color='property_type',
                        color_discrete_sequence=px.colors.sequential.Rainbow, 
                        width=600, height=500)
        st.plotly_chart(fig_bar)

        
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        # Filtering based on property_type
        property_type = st.selectbox("Select the Property_type",df2["property_type"].unique())
        df3= df2[df2["property_type"] == property_type]
        df3.reset_index(drop= True, inplace= True)

        df_grby= pd.DataFrame(df3.groupby("host_response_time")[["price","bedrooms"]].sum())
        df_grby.reset_index(inplace= True)

        fig_donut = px.pie(df_grby, values='price', names='host_response_time',
                hover_data=['bedrooms'],
                title='Price Difference Based on Host Response Time (Donut Chart)',
                color_discrete_sequence=px.colors.sequential.BuPu_r,
                hole=0.4,  # Size of the hole in the center
                width=800, height=500)
        
        st.plotly_chart(fig_donut)

        # Filtering based on host_response_time
        hostresponsetime= st.selectbox("Select the host_response_time",df3["host_response_time"].unique())
        df4 = df3[df3["host_response_time"] == hostresponsetime]

        fig_scatter = px.scatter(df4, x='minimum_nights', y='maximum_nights', color='bed_type',
                         size='price', hover_data=['price', 'bed_type'],
                         title=f'Scatter Plot: Minimum Nights vs Maximum Nights)',
                         color_discrete_sequence=px.colors.qualitative.Pastel1,
                         width=800, height=500)
        st.plotly_chart(fig_scatter)

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        df_grby= pd.DataFrame(df4.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
        df_grby.reset_index(inplace= True)

        fig_do_bar_2 = px.bar(df_grby, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Sunsetdark, width= 600, height= 500)
        st.plotly_chart(fig_do_bar_2)

    elif option == "Resource Assessment \U0001F4BB":
        def datafr():
            df_a= pd.read_csv("C:/Users/saich/OneDrive/Desktop/airbnb/Airbnb.csv")
            return df_a

        df_a= datafr()

        st.markdown("### AVAILABILITY ANALYSIS")

        # Get unique values for country and property type
        countries = df_a["country"].unique()
        property_types = df_a["property_type"].unique()

        # Streamlit UI for selecting country and property type
        country_a = st.selectbox("Select the Country_a", countries)
        property_ty_a = st.selectbox("Select the Property Type", property_types)

        # Filter DataFrame based on selected country and property type
        # Filter DataFrame based on selected country and property type
        df_filtered = df_a[(df_a["country"] == country_a) & (df_a["property_type"] == property_ty_a)]

        # Check and handle zero values in the availability columns
        avail_columns = ["availability_30", "availability_60", "availability_90", "availability_365"]
        for column in avail_columns:
            df_filtered[column] = df_filtered[column].replace(0, 0.01)  # Replace zero values with a small non-zero value

        color_scales = {
                            "availability_30": "Magenta",
                            "availability_60": "blues",
                            "availability_90": "tealrose",
                            "availability_365": "darkmint"
                        }

        # Iterate through each availability column and create a treemap chart with a custom color scale
        for avail_col in avail_columns:
            fig_treemap = px.treemap(df_filtered, path=["room_type", "bed_type", "is_location_exact"],
                                    values=avail_col,
                                    title=f"{avail_col.capitalize()} Treemap",
                                    color=avail_col,
                                    color_continuous_scale=color_scales.get(avail_col, "Viridis"),  # Use custom color scale or fallback to Viridis
                                    hover_data=["is_location_exact", avail_col],
                                    width=800, height=500)
            
            # Show the treemap chart in Streamlit
            st.plotly_chart(fig_treemap)
        

        roomtype_a= st.selectbox("Select the Room Type_a", df_filtered["room_type"].unique())

        df3_a= df_filtered[df_filtered["room_type"] == roomtype_a]

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Sunsetdark_r,width=1000)

        st.plotly_chart(fig_df_mul_bar_a)

    elif option == "Location Based \U0001F5FA":
        
        st.markdown("### LOCATION BASED ANALYSIS")
        st.write("")

        def datafr():
            df= pd.read_csv("C:/Users/saich/OneDrive/Desktop/airbnb/Airbnb.csv")
            return df

        df_loc= datafr()   

        country_loc= st.selectbox("Select the Country_l",df_loc["country"].unique())

        df1_loc= df_loc[df_loc["country"] == country_loc]
        df1_loc.reset_index(drop= True, inplace= True)

        proper_ty_loc= st.selectbox("Select the Property_type_l",df1_loc["property_type"].unique())

        df2_loc= df1_loc[df1_loc["property_type"] == proper_ty_loc]
        df2_loc.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_loc[df2_loc["price"] <= differ_max_min*0.30 + df2_loc['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_loc['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_loc[df2_loc["price"] >= differ_max_min*0.30 + df2_loc['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_loc['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_loc['price'].min())+' '+str('to')+' '+str(df2_loc['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_loc[df2_loc["price"] >= differ_max_min*0.60 + df2_loc['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df2_loc['price'].max()-df2_loc['price'].min()

        val_sel= st.radio("Select the Price Range",[str(df2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_loc['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_loc['price'].min())+' '+str('to')+' '+str(df2_loc['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)


        # Creating a correlation matrix from the above dataframeby dropping the below columns

        df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
        
        st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Magenta,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Oryel,width=1000)
        st.plotly_chart(fig_3) 

    elif option == "Map-based Analysis \U0001F310":
        st.markdown("### GEOSPATIAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale= "Viridis",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4) 
    
    elif option == "Top Trends \U0001F4C8":
        st.markdown("### TOP TRENDS")
        country_top= st.selectbox("Select the Country_t",df["country"].unique())

        df1_top= df[df["country"] == country_top]

        property_ty_t= st.selectbox("Select the Property_type_t",df1_top["property_type"].unique())

        df2_top= df1_top[df1_top["property_type"] == property_ty_t]
        df2_top.reset_index(drop= True, inplace= True)

        df2_top_sorted= df2_top.sort_values(by="price")
        df2_top_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_top_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Average_price"]
        
        # Total_price based on Host_neighbourhood
        fig_price_pie = px.pie(df_price, values='Total_price', names='host_neighbourhood', title='TOTAL PRICE BASED ON HOST_NEIGHBOURHOOD')
        st.plotly_chart(fig_price_pie)


        # Average Price based on Host_neighbourhood
        fig_price_pie2= px.pie(df_price, values = "Average_price", names= "host_neighbourhood", 
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD")
        st.plotly_chart(fig_price_pie2)

        df_price_1= pd.DataFrame(df2_top_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
        df_price_1.reset_index(inplace= True)
        df_price_1.columns= ["host_location", "Total_price", "Average_price"]

        # Total_price based on Host_location
        fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                            width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Sunsetdark_r,
                            title= "TOTAL PRICE BASED ON HOST_LOCATION")
        st.plotly_chart(fig_price_3)

        # Average_price based on Host_location
        fig_price_4= px.bar(df_price_1, x= "Average_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Magma_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
        st.plotly_chart(fig_price_4)

# Project Overview
elif select == "Project Overview \U0001F310":

    st.markdown("## Welcome to the Project Overview Section \U0001F310")
    st.write("")
    st.markdown("#### Problem Statement \U0001F4AD")
    st.write("\U00002728 This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. The objectives are as follows:")
    st.write("")
    st.markdown("#### Skills Takeaway \U0001F4CB")
    st.write("\U00002728 Python scripting")
    st.write("\U00002728 Data Preprocessing")
    st.write("\U00002728 Data Visualization")
    st.write("\U00002728 EDA")
    st.write("\U00002728 Streamlit")
    st.write("\U00002728 MongoDB")
    st.write("\U00002728 Power BI")

    st.write("")
    st.write("")
    st.markdown("#### Domain \U0001F310")
    st.write("\U00002728 Travel Industry")
    st.write("\U00002728 Property Management")
    st.write("\U00002728 Tourism")

    st.write("")
    st.write("")

    # Objectives
    st.markdown("#### Objectives \U0001F4CB")
    objectives = [
    "Establish a MongoDB connection and retrieve the Airbnb dataset.",
    "Clean and prepare the dataset for analysis.",
    "Develop a streamlit web application with interactive maps.",
    "Conduct price analysis and visualization.",
    "Analyze availability patterns across seasons.",
    "Investigate location-based insights.",
    "Create interactive visualizations and dashboards." ]

    for index, objective in enumerate(objectives, start=1): # used to loop over an iterable
        st.write(f"{index}. {objective}") # Prints the index (starting from 1) and the objective
    
    st.write("")
    st.write("")

    # Approach
    st.markdown("#### Approach \U0001F4DD")
    approach = [
        "1. MongoDB Connection and Data Retrieval",
        "2. Data Cleaning and Preparation",
        "3. Geospatial Visualization",
        "4. Price Analysis and Visualization",
        "5. Availability Analysis by Season",
        "6. Location-Based Insights",
        "7. Interactive Visualizations",
        "8. Dashboard Creation" ]
    
    for index, step in enumerate(approach, start=1):
        st.write(f"{index}. {step}")

    st.write("")
    st.write("")

    # Outcomes
    st.markdown("#### Learning Outcomes \U0001F4DA")
    outcomes = [
        "MongoDB Atlas",
        "Streamlit Web Application",
        "Python Data Analysis",
        "Geospatial Analysis",
        "Tableau or Power BI",
        "Data Cleaning and Preparation",
        "Data Visualization Techniques",
        "Problem-Solving Skills",
        "Data-Driven Decision Making",
        "Collaboration and Project Management"]
    
    for index, outcome in enumerate(outcomes, start=1):
        st.write(f"{index}. {outcome}")