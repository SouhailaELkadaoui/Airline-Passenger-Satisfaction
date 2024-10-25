import streamlit as st
import joblib
import numpy as np

# Charger le modèle de prédiction
model = joblib.load("Airline_Passenger_Satisfaction_model.joblib")

# Titre de l'application
st.title("Prédiction de la Satisfaction du Client")

# Formulaire pour entrer les caractéristiques d'un client
st.write("Entrez les caractéristiques du client :")

gender = st.selectbox("Genre", [0, 1])  # 0 pour féminin, 1 pour masculin
customer_type = st.selectbox("Type de client", [0, 1])  # 0 pour nouveau, 1 pour loyal
type_of_travel = st.selectbox("Type de voyage", [0, 1])  # 0 pour personnel, 1 pour affaires
class_of_travel = st.selectbox("Classe de voyage", [0.0, 1.0, 2.0])  # 0 pour Eco, 1 pour Eco Plus, 2 pour Business
age = st.number_input("Âge", min_value=0, max_value=100, value=30)
flight_distance = st.number_input("Distance de vol", min_value=0)

inflight_wifi_service = st.slider("Service Wi-Fi en vol (1-5)", min_value=1, max_value=5, value=3)
departure_arrival_convenient = st.slider("Confort départ/arrivée (1-5)", min_value=1, max_value=5, value=3)
ease_of_online_booking = st.slider("Facilité de réservation en ligne (1-5)", min_value=1, max_value=5, value=3)
gate_location = st.slider("Emplacement de la porte (1-5)", min_value=1, max_value=5, value=3)

# Ajout de la caractéristique Food and Drink
food_and_drink = st.slider("Service de nourriture et boisson (1-5)", min_value=1, max_value=5, value=3)

online_boarding = st.slider("Embarquement en ligne (1-5)", min_value=1, max_value=5, value=3)
seat_comfort = st.slider("Confort du siège (1-5)", min_value=1, max_value=5, value=3)
inflight_entertainment = st.slider("Divertissement en vol (1-5)", min_value=1, max_value=5, value=3)
onboard_service = st.slider("Service à bord (1-5)", min_value=1, max_value=5, value=3)
leg_room_service = st.slider("Service d'espace pour les jambes (1-5)", min_value=1, max_value=5, value=3)
baggage_handling = st.slider("Manutention des bagages (1-5)", min_value=1, max_value=5, value=3)
checkin_service = st.slider("Service d'enregistrement (1-5)", min_value=1, max_value=5, value=3)
inflight_service = st.slider("Service en vol (1-5)", min_value=1, max_value=5, value=3)
cleanliness = st.slider("Propreté (1-5)", min_value=1, max_value=5, value=3)
total_delay = st.number_input("Délai total (en minutes)", min_value=0.0)

# Rassembler les données sous forme de tableau pour le modèle
client_data = np.array([[gender, customer_type, type_of_travel, class_of_travel, age, flight_distance,
                         inflight_wifi_service, departure_arrival_convenient, ease_of_online_booking, gate_location,
                         food_and_drink, online_boarding, seat_comfort, inflight_entertainment, onboard_service,
                         leg_room_service, baggage_handling, checkin_service, inflight_service, cleanliness,
                         total_delay]])

# Bouton pour effectuer la prédiction
if st.button("Prédire la satisfaction"):
    # Faire la prédiction avec le modèle
    prediction = model.predict(client_data)
    
    # Afficher le résultat de la prédiction
    if prediction[0] == 0:
        st.error("Le client n'est pas satisfait ou neutre.")
    elif prediction[0] == 1:
        st.info("Le client est très satisfait.")
