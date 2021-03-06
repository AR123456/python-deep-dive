## MORE CODE ABOVE

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for("secrets"))

    return render_template("register.html")

## MORE CODE BELOW