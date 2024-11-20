import discord
import random
import json
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import os

def main():
    # Charger l'environnement depuis le fichier .env
    load_dotenv()

    # Charger et sauvegarder les scores
    def load_scores():
        try:
            with open('scores.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_scores(scores):
        with open('scores.json', 'w') as file:
            json.dump(scores, file, indent=4)

    # Charger les défis hebdomadaires
    def load_weekly_challenges():
        try:
            with open('weekly_challenges.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_weekly_challenges(challenges):
        with open('weekly_challenges.json', 'w') as file:
            json.dump(challenges, file, indent=4)

    # Charger les preuves en attente
    def load_pending_proofs():
        try:
            with open('pending_proofs.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_pending_proofs(proofs):
        with open('pending_proofs.json', 'w') as file:
            json.dump(proofs, file, indent=4)

    # Charger les données au démarrage
    scores = load_scores()
    weekly_challenges = load_weekly_challenges()
    pending_proofs = load_pending_proofs()

    # Liste des défis
    challenges = [
        "Gagner une partie avec 25 kills minimum sur 3 parties différentes.",
    "Gagner une partie avec au moins 35 kills sur une seule map.",
    "Gagner une partie où chaque membre de l'équipe a au moins 10 kills.",
    "Gagner 3 parties consécutives en étant MVP.",
    "Gagner une partie avec 20 kills minimum.",
    "Gagner une partie avec au moins 15 kills sur chaque map jouée dans la semaine.",
    "Réaliser au total 150 kills dans l'historique de partie.",
    "Gagner une partie avec 30 kills minimum.",
    "Gagner une partie avec un K/D supérieur à 3 dans 3 parties différentes.",
    "Gagner une partie avec un K/D supérieur à 4 sur une map spécifique (par exemple, Haven).",
    "Gagner une partie avec un K/D de moins de 1.",
    "Gagner 5 parties avec un K/D supérieur à 2.",
    "Réussir 2 games consécutives avec un K/D supérieur à 2.0.",
    "Gagner une partie avec un pourcentage de headshot supérieur à 40%.",
    "Gagner une partie en réalisant au moins 50 pourcents de headshots dans une manche.",
    "Gagner une partie en réalisant 15 assists minimum.",
    "Réaliser au moins 80 assists dans l'historique de partie.",
    "Réussir 5 assists en une seule manche et gagner la partie.",
    "Avoir 15 assists ou plus sur 3 parties gagnées différentes.",
    "Gagner une partie en ayant le plus grand nombre d'assists parmi les deux équipes.",
    "Gagner une partie avec un écart de 10 rounds ou plus.",
    "Gagner une partie avec un score exact de 13-11.",
    "Gagner une partie avec 0 rounds perdus en attaque.",
    "Gagner une partie en étant mené 9-3, puis remonter pour gagner.",
    "Gagner une partie avec 6 manches consécutives sans perdre un round.",
    "Gagner 2 parties consécutives avec au moins 10 rounds d'écart.",
    "Gagner une partie sur chaque map au moins une fois.",
    "Gagner une partie avec 4 agents dans l'historique.",
    "Gagner une partie en jouant un agent Initiateur avec au moins 10 assists.",
    "Gagner une partie en jouant un agent Dueliste avec 20 kills.",
    "Gagner une partie avec Sage en réalisant au moins 3 résurrections.",
    "Gagner une partie avec Killjoy en obtenant au moins 2 kills grâce à ses molly.",
    "Gagner une partie avec Raze et réaliser un double kill avec son ultime.",
    "Gagner une partie avec Brimstone et obtenir au moins 2 kills avec ses grenades incendiaires.",
    "Gagner une partie avec Sova en réalisant au moins 5 kills à travers des murs.",
    "Gagner une partie avec Jett en réalisant au moins 5 kills avec son ultime.",
    "Gagner une partie avec Cypher en réalisant au moins 5 kills à travers des smokes.",
    "Gagner une partie où chaque membre de l'équipe réalise au moins 10 kills.",
    "Gagner une partie où l'équipe entière ne perd aucun round en défense.",
    "Gagner une partie avec au moins 2 kills par round sur 5 rounds consécutifs.",
    "Gagner 3 parties consécutives.",
    "Gagner 5 parties consécutives.",
    "Gagner 7 parties consécutives.",
    "Gagner un partie en faisant un ACE.",
    "Gagner une partie où vous réalisez 2 clutch consécutifs.",
    "Gagner une partie après avoir perdu tous les pistol rounds.",
    "Gagner une partie en ayant participé à 50 pourcents des kills ou assists de l’équipe.",
    ]

    # Initialisation du bot
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Le bot est maintenant connecté : {client.user.name} (ID: {client.user.id})")
        await trouver_ou_creer_channels()

    # Chercher ou créer les canaux nécessaires
    async def trouver_ou_creer_channels():
        for guild in client.guilds:
            for channel_name in ["apobjectif", "preuve"]:
                channel = discord.utils.get(guild.text_channels, name=channel_name)
                if not channel:
                    await guild.create_text_channel(channel_name)
                    print(f"✅ Canal '{channel_name}' créé dans : {guild.name}")
                else:
                    print(f"✅ Canal '{channel_name}' trouvé dans : {guild.name}")

    @client.event
    async def on_message(message):
        # Ignorer les messages du bot lui-même
        if message.author == client.user:
            return

        # Limiter les commandes aux canaux autorisés
        if message.channel.name not in ["apobjectif", "preuve"]:
            return

        user_id = str(message.author.id)

        # Commande : Afficher les défis hebdomadaires
        if message.content == "!défi":
            if weekly_challenges:
                response = "**🎯 Défis hebdomadaires 🎯**\n\n"
                for i, defi in enumerate(weekly_challenges, start=1):
                    response += f"{i}. {defi}\n"
                await message.channel.send(response)
            else:
                await message.channel.send("Aucun défi hebdomadaire n'est actuellement défini.")

        # Commande : Afficher ses points
        elif message.content == "!stat":
            if user_id not in scores:
                scores[user_id] = {"points": 0}
                save_scores(scores)
            points = scores[user_id]["points"]
            await message.channel.send(f"✅ {message.author.mention}, vous avez actuellement **{points} points**.")

        # Commande : Afficher le classement
        elif message.content == "!classement":
            classement = sorted(scores.items(), key=lambda x: x[1].get("points", 0), reverse=True)
            if classement:
                response = "**🏆 Classement des meilleurs joueurs 🏆**\n\n"
                for i, (user, data) in enumerate(classement[:10], start=1):
                    points = data.get("points", 0)
                    response += f"{i}. <@{user}> : {points} points\n"
                await message.channel.send(response)
            else:
                await message.channel.send("❌ Aucun joueur enregistré dans le classement.")

        # Commande : Ajouter des points
        elif message.content.startswith("!ajouterpoints"):
            if "mod" in [role.name.lower() for role in message.author.roles]:
                try:
                    _, utilisateur, points = message.content.split()
                    points = int(points)
                    utilisateur_id = utilisateur.strip("<@!>")
                    if utilisateur_id not in scores:
                        scores[utilisateur_id] = {"points": 0}
                    scores[utilisateur_id]["points"] += points
                    save_scores(scores)
                    user_object = await message.guild.fetch_member(utilisateur_id)
                    await message.channel.send(f"✅ {points} points ajoutés à {user_object.mention}.")
                except ValueError:
                    await message.channel.send("❌ Utilisation : !ajouterpoints <@utilisateur> <points>")
            else:
                await message.channel.send("❌ Vous n'avez pas les permissions pour utiliser cette commande.")

        # Commande : Enlever des points
        elif message.content.startswith("!enleverpoints"):
            if "mod" in [role.name.lower() for role in message.author.roles]:
                try:
                    _, utilisateur, points = message.content.split()
                    points = int(points)
                    utilisateur_id = utilisateur.strip("<@!>")
                    if utilisateur_id not in scores:
                        scores[utilisateur_id] = {"points": 0}
                    scores[utilisateur_id]["points"] -= points
                    if scores[utilisateur_id]["points"] < 0:
                        scores[utilisateur_id]["points"] = 0
                    save_scores(scores)
                    user_object = await message.guild.fetch_member(utilisateur_id)
                    await message.channel.send(f"✅ {points} points enlevés à {user_object.mention}.")
                except ValueError:
                    await message.channel.send("❌ Utilisation : !enleverpoints <@utilisateur> <points>")
            else:
                await message.channel.send("❌ Vous n'avez pas les permissions pour utiliser cette commande.")

        # Commande : Réinitialiser les scores
        elif message.content == "!resetscores":
            if "mod" in [role.name.lower() for role in message.author.roles]:
                scores.clear()
                save_scores(scores)
                await message.channel.send("✅ Tous les scores ont été réinitialisés.")
            else:
                await message.channel.send("❌ Vous n'avez pas les permissions pour utiliser cette commande.")

        # Commande : Changer les défis
        elif message.content == "!changerdefis":
            if "mod" in [role.name.lower() for role in message.author.roles]:
                weekly_challenges.clear()
                weekly_challenges.extend(random.sample(challenges, 10))
                save_weekly_challenges(weekly_challenges)
                response = "**🎯 Nouveaux défis hebdomadaires 🎯**\n\n"
                for i, defi in enumerate(weekly_challenges, start=1):
                    response += f"{i}. {defi}\n"
                await message.channel.send(response)
            else:
                await message.channel.send("❌ Vous n'avez pas les permissions pour utiliser cette commande.")

        # Commande : Soumettre une preuve
        elif message.content.startswith("!preuve"):
            try:
                _, defi_num, lien = message.content.split(maxsplit=2)
                defi_num = int(defi_num)
                if defi_num <= 0 or defi_num > len(weekly_challenges):
                    await message.channel.send("❌ Numéro de défi invalide.")
                    return
                pending_proofs.append({
                    "utilisateur": user_id,
                    "defi": defi_num,
                    "lien": lien
                })
                save_pending_proofs(pending_proofs)
                proof_channel = discord.utils.get(client.get_all_channels(), name="preuve")
                if proof_channel:
                    await proof_channel.send(
                        f"🔔 **Nouvelle preuve soumise !**\n"
                        f"- Utilisateur : {message.author.mention}\n"
                        f"- Défi : {weekly_challenges[defi_num - 1]}\n"
                        f"- Lien : {lien}\n"
                        f"Les modérateurs peuvent valider cette preuve avec `!validerdefi <utilisateur> <numéro_du_défi>`."
                    )
                await message.channel.send("✅ Preuve envoyée avec succès et en attente de validation.")
            except ValueError:
                await message.channel.send("❌ Utilisation : !preuve <numéro_du_défi> <lien>")

        # Commande : Valider une preuve
        elif message.content.startswith("!validerdefi"):
            if "mod" in [role.name.lower() for role in message.author.roles]:
                try:
                    _, utilisateur, defi_num = message.content.split()
                    defi_num = int(defi_num)
                    utilisateur_id = utilisateur.strip("<@!>")
                    matching_proof = next(
                        (proof for proof in pending_proofs if proof["utilisateur"] == utilisateur_id and proof["defi"] == defi_num),
                        None
                    )
                    if matching_proof:
                        if utilisateur_id not in scores:
                            scores[utilisateur_id] = {"points": 0}
                        scores[utilisateur_id]["points"] += 10
                        save_scores(scores)
                        pending_proofs.remove(matching_proof)
                        save_pending_proofs(pending_proofs)
                        user_object = await message.guild.fetch_member(utilisateur_id)
                        await message.channel.send(f"✅ Défi {defi_num} validé pour {user_object.mention} !")
                    else:
                        await message.channel.send("❌ Aucune preuve correspondante trouvée.")
                except ValueError:
                    await message.channel.send("❌ Utilisation : !validerdefi <utilisateur> <numéro_du_défi>")
            else:
                await message.channel.send("❌ Vous n'avez pas les permissions pour utiliser cette commande.")

        # Commande : Afficher l'aide
        elif message.content == "!aide":
            response = (
                "**🛠 Commandes Disponibles 🛠**\n"
                "`!défi` : Affiche les défis hebdomadaires.\n"
                "`!classement` : Affiche le classement des joueurs.\n"
                "`!stat` : Affiche vos points actuels.\n"
                "`!preuve <numéro_du_défi> <lien>` : Soumet une preuve pour un défi.\n"
                "`!validerdefi <utilisateur> <numéro_du_défi>` : Valide une preuve (modérateurs uniquement).\n"
                "`!ajouterpoints <utilisateur> <points>` : Ajoute des points à un utilisateur (modérateurs uniquement).\n"
                "`!enleverpoints <utilisateur> <points>` : Enlève des points à un utilisateur (modérateurs uniquement).\n"
                "`!resetscores` : Réinitialise tous les scores (modérateurs uniquement).\n"
                "`!changerdefis` : Change les défis hebdomadaires (modérateurs uniquement).\n"
                "`!aide` : Affiche cette liste de commandes.\n"
            )
            await message.channel.send(response)

    client.run(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    main()