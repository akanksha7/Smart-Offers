
import streamlit as st 
import numpy as np
import pandas as pd

df = pd.read_csv("/usercode/Clustered_data.csv")

def get_recommendations(User, num_of_rec) :
    try :
        Cluster = df[df["CustomerID"]==int(User)]["Cluster"].unique()[0]
        df_cluster = df[df["Cluster"]==Cluster]
        df_cluster = df_cluster.groupby("MerchantName")["TransactionValue"].sum().nlargest(int(num_of_rec))
        for index , mer in enumerate(df_cluster.index):
            st.text(f"Recommendation number {index+1} of user {User} is {mer}")
    except:
        st.text(f"The User {User} is not exist on the dataset")
        
def main():
    st.title("Personalized Recommendation")
    User = st.text_input("Enter User Id")
    num_of_rec = st.text_input("Enter num of Rec")
    if st.button("Recommend"):
        get_recommendations(User, num_of_rec)

main()
