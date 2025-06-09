import streamlit as st
import requests
from datetime import datetime
from services.api import send_to_ai

# Ολοκλήρωση αγοράς και αποστολή στο backend + AI
def render_purchase_section():
    # Εμφάνιση προηγούμενης συνταγής (αν υπάρχει)
    if "last_recipe" in st.session_state and st.session_state.last_recipe:
        st.subheader("🍽️ Συνταγή:")
        st.markdown(st.session_state.last_recipe)
        st.subheader("🥗 Διατροφική Αξιολόγηση:")
        st.markdown(st.session_state.last_nutrition)

#Αν δεν υπαρχει καλαθι,δεν συνεχιζει
    if not st.session_state.cart:
        return
    
    #Κουμπί για συνταγή πριν την αγορά
    if st.button("👨‍🍳 Πρότεινέ μου συνταγές με βάση το καλάθι"):
        item_list = [
            {"name": name, "category": item["category"], "price": item["price"]}
            for name, item in st.session_state.cart.items()
        ]
        # Κλήση AI πριν το POST στην αγορά
        ai_result = send_to_ai(item_list)
        if ai_result:
            st.session_state.last_recipe = ai_result.get("recipe", "❌ Δεν επιστράφηκε συνταγή.")
            st.session_state.last_nutrition = ai_result.get("nutrition", "❌ Δεν επιστράφηκε αξιολόγηση.")
            st.rerun()
        else:
            st.error("❌ Το AI σύστημα δεν απάντησε.")

    #Κουμπί για ολοκλήρωση αγοράς
    if st.button("Ολοκλήρωση αγοράς"):
        purchase = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": st.session_state.cart.copy()
        }
        st.session_state.history.append(purchase)

        try:
            res = requests.post("http://localhost:5050/purchase", json=purchase)
            if res.status_code == 200:
                st.success("Η αγορά ολοκληρώθηκε!")
                st.session_state.cart.clear()
                st.rerun()
            else:
                st.error("❌ Η αποστολή της αγοράς απέτυχε.")
        except Exception as e:
            st.error(f"⚠️ Δεν μπόρεσα να συνδεθώ με το backend: {e}")
     
        
        
# # Εναλλακτικό κουμπί για συνταγές ai
#     if st.button("👨‍🍳 Πρότεινέ μου συνταγές με βάση την τελευταία αγορά"):
#         if "last_recipe" in st.session_state:
#             st.subheader("🍽️ Συνταγή:")
#             st.markdown(st.session_state.last_recipe)
#             st.subheader("🥗 Διατροφική Αξιολόγηση:")
#             st.markdown(st.session_state.last_nutrition)
#         else:
#             st.info("Δεν υπάρχει ακόμη αποθηκευμένη συνταγή.")