import streamlit as st

st.header("Matahri dan Bulan") #untuk membuat header
st.subheader("Matahari menyinari Bulan yang redup") #untuk membuat subjudul yang lebih kecil
st.text("Bulan dan matahari begitu indah") #untuk membuat text polos tanpa format
st.markdown("**Tebal** dan *Miring*") #markdown untuk memformat teks tebal/miring
st.caption("caption") #teks kecil dari bawah elemen
st.title("Matahari dan Bulan") #untuk menampilkan judul utama

#Bagian 1
st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1 : Teks Element")
st.markdown("""
            1. Distia Fajar Familiati - 0110222163
            2. Sabrina Ramadhani - 0110222068
            3. Muhammad Fariz Zacky- 011022227 """)

#Bagian 2 : menampilkan rumus latex
st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus binominal

#Bagian 3 : Menampilkan kode program
st.header("Displaying Code")
st.subheader("Python Code")

#simpan ke variabel
code = '''
def hello :
    print("Hello, Streamlit!")
    '''

#st.code() tampilkan potongan kode dengan format rapi
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
        public class GFG {
            public static void main{string arg[]} {
                system.out.printIn("Hello world!");
                }
        }
        """, language='java')
#fungsi st.code() bisa untuk bahasa pemrograman lain

st.subheader("Javascript Code")
st.code("""
        <script>
        try {
            addalert("Welcome Guest"); // kesalahan ketik (addalert) sengaja dibuat untuk menimbulkan error
        }
        catch(err) {
            document.getElementById("demo").innerHTML = err.message; // menampilkan pesan error di elemen HTML dengan id 'demo'
        }
        </script>
        """, language='javascript')
# Kode hanya contoh bagaimana menangani error (exception) di JavaScript
# Hasilnya tidak dijalankan di streamlit, hanya display contoh kode