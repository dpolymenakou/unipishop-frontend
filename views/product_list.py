import streamlit as st
from services.api import scraping_bazaar, scraping_marktin



# Εμφάνιση λίστας προϊόντων με δυνατότητα προσθήκης στο καλάθι
def render_product_list(filtered_products):
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    st.subheader("🛍️ Προϊόντα προς επιλογή")

 # Προϊόντα και ποσότητες  
    for idx, product in enumerate(filtered_products):
        with st.container():
            col1, col2 = st.columns([4, 1])

            with col1:
                try:
                    st.image("http://localhost:5050" + product["image"], width=100)
                except:
                    st.image("https://via.placeholder.com/100?text=No+Image", width=100)

                st.markdown(f"**{product['name']}** — *{product['category']}*")
                st.markdown(f"💶 Τιμή: **{product['price']} €**")
                st.markdown(f"📄 _{product['description']}_")
               
               # Κουμπί για scraping τιμών
                if st.button(f"🔍 Σύγκριση Τιμών ({product['name']})", key=f"compare_{idx}"):

                    # --- Bazaar ---
                    img_baz, price_baz, desc_baz = scraping_baz(product["name"])
                    with st.expander("🛒 Bazaar"):
                        if img_baz:
                            st.image(img_baz, width=100)
                        st.write(f"💶 Τιμή: {price_baz}")
                        st.write(f"📄 {desc_baz}")

                    # --- Scraping Market-In ---
                    img_markt, price_markt, desc_markt = scraping_marktin(product["name"])
                    with st.expander("🛍️ Market-In"):
                        if img_markt:
                            st.image(img_markt, width=100)
                        st.write(f"💶 Τιμή: {price_markt}")
                        st.write(f"📄 {desc_markt}")
                
            with col2:
                qty = st.number_input("Ποσότητα", min_value=1, max_value=10, step=1, key=f"qty_{idx}")
                if st.button("Προσθήκη", key=f"add_{idx}"):
                    pname = product["name"]
                    if pname in st.session_state.cart:
                        st.session_state.cart[pname]["qty"] += qty
                    else:
                        st.session_state.cart[pname] = {
                            "qty": qty,
                            "price": product["price"],
                            "category": product["category"] 
                        }
                    st.success(f"✅ Προστέθηκαν {qty} τεμάχια από το {pname}")

