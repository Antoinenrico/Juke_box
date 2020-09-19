function send_Gcode_to_motor(sens) {
    if ((sens == "gauche") || (sens == "init") || (sens == "parametres") || (sens == "droite") || (sens == "haut") || (sens == "bas")) {
        // Zone de texte où écrire le log des actions
        const zone_text = document.getElementById("msg")

        // Créer une requête
        let req = new XMLHttpRequest();
        // Définir l'action à prendre une fois la réponse du serveur reçue
        req.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                //  Si succès, écrire le status + le message reçu sur la page
                zone_text.innerText += this.status + " - " + this.responseText + "\n"
            } else if (this.readyState == 4) {
                //  Si erreur, écrire l'erreur sur la page
                zone_text.innerText += this.status + " - Erreur: " + this.responseText + "\n"
            }
        }
        req.open('POST', '/api', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("sens=" + sens);
    }
}
