# import streamlit as st
# import requests 
# debug_mode = True    #devmode

# # URL του backend Flask API
# BACKEND_URL = "http://127.0.0.1:5050"

# # Mock προϊόντα
# #products = [
#     #{"name": "Γάλα", "category": "Τρόφιμα", "price": 1.5},
#     #{"name": "Τυρί", "category": "Τρόφιμα", "price": 3.2},
#     #{"name": "Ψωμί", "category": "Τρόφιμα", "price": 1.0},
#     #{"name": "Καφές", "category": "Ροφήματα", "price": 4.0},
#     #{"name": "Χυμός Πορτοκάλι", "category": "Ροφήματα", "price": 2.5},
#     #{"name": "Ζάχαρη", "category": "Είδη Σπιτιού", "price": 1.2},
#     #{"name": "Αλεύρι", "category": "Είδη Σπιτιού", "price": 1.8},
#     #{"name": "Μπανάνα", "category": "Φρούτα", "price": 0.6},
#     #{"name": "Μήλο", "category": "Φρούτα", "price": 0.7},]

#  #Αντικατάσταση μοκ με πραγματικα δεδομενα απο mongo
# try:
#     response = requests.get(f"{BACKEND_URL}/getallproducts")
#     if response.status_code == 200:
#         products = response.json()
#     else:
#         st.error("❌ Σφάλμα κατά τη λήψη των προϊόντων από το backend.")
#         products = []
# except Exception as e:
#     st.error(f"⚠️ Το backend δεν είναι διαθέσιμο: {e}")
#     products = []

# # Αρχικοποίηση καλαθιού 
# if "cart" not in st.session_state:  # session για να αποθηκεύουμε το καλάθι 
#     st.session_state.cart = {}

# # Αρχικοποίηση ιστορικού αγορών (τοπικά στο session)
# if "history" not in st.session_state:
#     st.session_state.history = []

# st.title("🛒 SmartCart - UnipiShop")

# st.header("🔍Φίλτρα Αναζήτησης")

# #Κατηγορίες προϊόντων
# categories = list(set([p["category"] for p in products]))
# categories.sort()
# categories.insert(0, "Όλες")

# # Επιλογή φίλτρων
# #selected_category = st.selectbox("Φίλτρο κατηγορίας:", categories)
# #search_query = st.text_input("Αναζήτηση προϊόντος:")
# #sort_option = st.selectbox("Ταξινόμηση:", ["Χωρίς ταξινόμηση", "Αλφαβητικά (Α-Ω)", "Αλφαβητικά (Ω-Α)", "Τιμή (αύξουσα)", "Τιμή (φθίνουσα)"])

# # Εφαρμογή φίλτρων
# #filtered_products = products

# # Αρχικοποίηση προϊόντων προς φιλτράρισμα
# filtered_products = products.copy()

# # Φίλτρο κατηγορίας
# selected_category = st.selectbox("Φίλτρο κατηγορίας:", categories, key="category_select")
# if selected_category != "Όλες":
#     filtered_products = [p for p in filtered_products if p["category"] == selected_category]
#     subcategories = sorted(set(p["subcategory"] for p in filtered_products))
#     subcategories.insert(0, "Όλες")
#     selected_subcategory = st.selectbox("Φίλτρο υποκατηγορίας:", subcategories, key="subcategory_select")
# else:
#     selected_subcategory = "Όλες"

# # Φίλτρο υποκατηγορίας
# if selected_subcategory != "Όλες":
#     filtered_products = [p for p in filtered_products if p["subcategory"] == selected_subcategory]
                                                           
# # Φίλτρο λέξης/Αναζήτηση
# search_query = st.text_input("Αναζήτηση προϊόντος:", key="search_input")
# if search_query:
#     filtered_products = [p for p in filtered_products if search_query.lower() in p["name"].lower()]

# # Ταξινόμηση
# sort_option = st.selectbox(
#     "Ταξινόμηση:",
#     ["Χωρίς ταξινόμηση", "Αλφαβητικά (Α-Ω)", "Αλφαβητικά (Ω-Α)", "Τιμή (αύξουσα)", "Τιμή (φθίνουσα)"], key="sort_option")
# if sort_option == "Αλφαβητικά (Α-Ω)":
#     filtered_products = sorted(filtered_products, key=lambda x: x["name"])
# elif sort_option == "Αλφαβητικά (Ω-Α)":
#     filtered_products = sorted(filtered_products, key=lambda x: x["name"], reverse=True)
# elif sort_option == "Τιμή (αύξουσα)":
#     filtered_products = sorted(filtered_products, key=lambda x: x["price"])
# elif sort_option == "Τιμή (φθίνουσα)":
#     filtered_products = sorted(filtered_products, key=lambda x: x["price"], reverse=True)

# # Κενό πριν την εμφάνιση προϊόντων
# st.markdown("<br><br>", unsafe_allow_html=True)
# st.divider()
# st.subheader("🛍️ Προϊόντα προς επιλογή")


#     # Προϊόντα και ποσότητες
# for idx, product in enumerate(filtered_products): 
#     with st.container():
#         col1, col2 = st.columns([4, 1])
#         with col1:
#             try:
#                 st.image("http://localhost:5050" + product["image"], width=100)
#             except:
#                 st.image("https://via.placeholder.com/100?text=No+Image", width=100)
#             st.markdown(f"**{product['name']}** — *{product['category']}*")
#             st.markdown(f"💶 Τιμή: **{product['price']} €**")
#             st.markdown(f"📄 _{product['description']}_")
#         with col2:
#             qty = st.number_input(
#                 f"Ποσότητα", min_value=1, max_value=10, step=1, key=f"qty_{idx}"
#             )
#             if st.button("Προσθήκη", key=f"add_{idx}"):   #κουμπι προσθήκη στο καλάθι
#                 pname = product["name"]
#                 if pname in st.session_state.cart: # Αν υπάρχει ήδη αυξάνεται η ποσότητ
#                     st.session_state.cart[pname]["qty"] += qty
#                 else:
#                     st.session_state.cart[pname] = {"qty": qty,"price": product["price"],"category": product["category"]}
#                 st.success(f"✅ Προστέθηκαν {qty} τεμάχια από το {pname}")


# # Διαχωριστικό πριν το καλάθι
# st.divider()
# st.subheader("🧺 Το καλάθι μου")

# if st.session_state.cart:
#     total = 0
#     remove_keys = []  # Αυτά θα αφαιρεθούν

#     for name, item in st.session_state.cart.items():
#         subtotal = item["qty"] * item["price"]  # Ενδιάμεσο σύνολο

#         col1, col2 = st.columns([4, 1])  # 2 στήλες: για κείμενο & κουμπί

#         with col1:   # Όνομα, κατηγορία, ποσότητα
#             st.markdown(f"**{name}**<br><small>{item['qty']} τεμ.</small>", unsafe_allow_html=True)
#         with col2:  # Κουμπί αφαίρεσης προϊόντος
#             st.markdown(f"<span style='color:green'><b>{item['price']} €</b></span>", unsafe_allow_html=True)
#             if st.button(f"❌", key=f"remove_{name}"):
#                 remove_keys.append(name)

#         total += subtotal  # Συνολικό άθροισμα

#     # Διαγραφή προϊόντων που πατήθηκαν
#     for key in remove_keys:
#         del st.session_state.cart[key]

#     st.write(f"**Σύνολο: {total:.2f} €**")

#     # Κουμπί ολοκλήρωσης αγοράς
# from datetime import datetime

# if st.button("Ολοκλήρωση αγοράς"):
#     try:
#         # Δημιουργεί εγγραφή αγοράς με timestamp
#         purchase = {
#             "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "items": st.session_state.cart.copy()
#         }
        
#         #
#         #st.subheader("συνταγη")
#         #st.markdown

#         # Αποθήκευση στο τοπικό ιστορικό
#         st.session_state.history.append(purchase)

#         # Στέλνουμε στο backend
#         response = requests.post("http://localhost:5050/purchase", json=purchase)

#         if response.status_code == 200:
#             st.success("🧾 Η αγορά ολοκληρώθηκε και καταχωρήθηκε!")
#             st.session_state.cart.clear()
#         else:
#             st.error("❌ Η αποστολή της αγοράς απέτυχε.")

#         # Προσωρινή εμφάνιση για έλεγχο:
#         #st.write(st.session_state.history)

#     except Exception as e:
#         st.error(f"⚠️ Δεν μπόρεσα να συνδεθώ με το backend: {e}")

# #ιστορικο αγορών
# st.divider()
# st.subheader("Ιστορικό Αγορών")

# if st.session_state.history:
#     for entry in reversed(st.session_state.history):  # Το πιο πρόσφατο πάνω
#         st.markdown(f"**🕒 {entry['timestamp']}**")

#         total = 0
#         for name, item in entry["items"].items():
#             subtotal = item["qty"] * item["price"]
#             total += subtotal
#             st.markdown(f"• {name} — {item['qty']} τεμ. × {item['price']} € = {subtotal:.2f} €")

#         st.markdown(f"**Σύνολο: {total:.2f} €**")
#         st.markdown("---")
# else:
#     st.info("Δεν υπάρχει ακόμη ιστορικό αγορών.")

# recipe, nutri_val=post_cart_and_get_aiprompt(purchase)
# if st.button("👨‍🍳 Πρότεινέ μου συνταγές με βάση την τελευταία αγορά"):
#     if st.session_state.history:
#         last_purchase = st.session_state.history[-1]["items"]
#         item_list = [{"name": name, "category": item["category"], "price": item["price"]} for name, item in last_purchase.items()]
#         try:
#             res = requests.post("http://127.0.0.1:5050/finalcart", json=item_list)
#             if res.status_code == 200:
#                 data = res.json()
#                 st.subheader("🍽️ Συνταγές:")
#                 st.markdown(data["recipe"])
#                 st.subheader(" Διατροφική Αξιολόγηση:")
#                 st.markdown(data["nutrition"])
#             else:
#                 st.error("❌ Το AI σύστημα δεν απάντησε σωστά.")
#         except Exception as e:
#             st.error(f"⚠️ Πρόβλημα σύνδεσης με AI backend: {e}")
#     else:
#         st.info("Δεν υπάρχει ακόμα καμία ολοκληρωμένη αγορά.")

# #barchart
# import matplotlib.pyplot as plt
# from collections import defaultdict

# st.divider()
# st.subheader("📈 Γράφημα: Συχνότητα Προϊόντων σε Όλες τις Αγορές")

# # Υπολογισμός συνολικών ποσοτήτων για κάθε προϊόν
# product_counts = defaultdict(int)

# for entry in st.session_state.history:
#     for name, item in entry["items"].items():
#         product_counts[name] += item["qty"]

# if product_counts:
#     # Δημιουργία του bar chart
#     fig, ax = plt.subplots()
#     ax.bar(product_counts.keys(), product_counts.values())
#     ax.set_xlabel("Προϊόντα")
#     ax.set_ylabel("Συνολική Ποσότητα")
#     ax.set_title("Προϊόντα που αγοράστηκαν περισσότερο")

#     plt.xticks(rotation=45, ha='right')
#     plt.tight_layout()

#     st.pyplot(fig)
# else:
#     st.info("Δεν υπάρχουν αγορές για ανάλυση.")

#     #developer mode
# if debug_mode and st.session_state.history:
#     st.divider()
#     st.subheader("📊 Στατιστικά (Developer Only)")

#     import matplotlib.pyplot as plt

#     # Συγκεντρωτικά στοιχεία προϊόντων από το ιστορικό
#     product_totals = {}
#     for purchase in st.session_state.history:
#         for name, item in purchase["items"].items():
#             product_totals[name] = product_totals.get(name, 0) + item["qty"]

#     if product_totals:
#         fig, ax = plt.subplots()
#         ax.bar(product_totals.keys(), product_totals.values())
#         ax.set_title("Συνολικές Αγορές ανά Προϊόν")
#         ax.set_ylabel("Ποσότητα")
#         ax.set_xticklabels(product_totals.keys(), rotation=45, ha='right')
#         st.pyplot(fig)
#     else:
#         st.info("Δεν υπάρχουν δεδομένα για προβολή γραφήματος.")

















# #devmode -koumpi add delete product update grafimata 