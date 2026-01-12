from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import User, Notification
from clients.models import Client
from operations.models import Operation
from decimal import Decimal
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Génère des données fictives pour tester l\'application'

    def handle(self, *args, **options):
        self.stdout.write('Création des données fictives...')
        
        # Create users
        self.stdout.write('Création des utilisateurs...')
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            role='admin',
            first_name='Admin',
            last_name='Principal'
        )
        
        commercial1 = User.objects.create_user(
            username='commercial1',
            email='commercial1@example.com',
            password='commercial123',
            role='commercial',
            first_name='Jean',
            last_name='Dupont',
            phone='0601020304'
        )
        
        commercial2 = User.objects.create_user(
            username='commercial2',
            email='commercial2@example.com',
            password='commercial123',
            role='commercial',
            first_name='Marie',
            last_name='Martin',
            phone='0605060708'
        )
        
        commercials = [commercial1, commercial2]
        
        # Create clients
        self.stdout.write('Création des clients...')
        clients_data = [
            ('Dubois', 'Pierre', 'pierre.dubois@email.com', '0612345678', 'A'),
            ('Bernard', 'Sophie', 'sophie.bernard@email.com', '0623456789', 'A'),
            ('Petit', 'Lucas', 'lucas.petit@email.com', '0634567890', 'B'),
            ('Robert', 'Emma', 'emma.robert@email.com', '0645678901', 'B'),
            ('Richard', 'Thomas', 'thomas.richard@email.com', '0656789012', 'C'),
            ('Durand', 'Julie', 'julie.durand@email.com', '0667890123', 'C'),
            ('Leroy', 'Nicolas', 'nicolas.leroy@email.com', '0678901234', 'A'),
            ('Moreau', 'Claire', 'claire.moreau@email.com', '0689012345', 'B'),
            ('Simon', 'Antoine', 'antoine.simon@email.com', '0690123456', 'C'),
            ('Laurent', 'Camille', 'camille.laurent@email.com', '0601234567', 'A'),
            ('Lefebvre', 'Hugo', 'hugo.lefebvre@email.com', '0612345670', 'B'),
            ('Michel', 'Léa', 'lea.michel@email.com', '0623456701', 'C'),
            ('Garcia', 'Gabriel', 'gabriel.garcia@email.com', '0634567012', 'A'),
            ('David', 'Chloé', 'chloe.david@email.com', '0645670123', 'B'),
            ('Bertrand', 'Louis', 'louis.bertrand@email.com', '0656701234', 'C'),
        ]
        
        clients = []
        for nom, prenom, email, tel, type_c in clients_data:
            client = Client.objects.create(
                nom=nom,
                prenom=prenom,
                email=email,
                telephone=tel,
                type_client=type_c,
                commercial=random.choice(commercials)
            )
            clients.append(client)
        
        # Create operations
        self.stdout.write('Création des opérations...')
        operation_types = ['collecte', 'depot', 'retrait']
        statuses = ['en_attente', 'en_cours', 'terminee', 'annulee']
        
        # Generate operations for the last 12 months
        today = datetime.now().date()
        for i in range(150):
            days_ago = random.randint(0, 365)
            operation_date = today - timedelta(days=days_ago)
            
            Operation.objects.create(
                client=random.choice(clients),
                type_operation=random.choice(operation_types),
                montant=Decimal(random.uniform(100, 10000)).quantize(Decimal('0.01')),
                status=random.choice(statuses) if days_ago > 30 else random.choice(['en_cours', 'terminee']),
                description=f"Opération du {operation_date.strftime('%d/%m/%Y')}",
                date_operation=operation_date,
                created_by=random.choice(commercials + [admin])
            )
        
        # Create notifications
        self.stdout.write('Création des notifications...')
        notification_titles = [
            'Nouvelle opération enregistrée',
            'Client ajouté',
            'Objectif mensuel atteint',
            'Rappel: Suivi client',
            'Alerte: Opération en retard',
        ]
        
        for user in [admin, commercial1, commercial2]:
            for i in range(5):
                Notification.objects.create(
                    user=user,
                    title=random.choice(notification_titles),
                    message=f"Message de notification {i+1} pour {user.username}",
                    is_read=random.choice([True, False])
                )
        
        self.stdout.write(self.style.SUCCESS('✓ Données fictives créées avec succès!'))
        self.stdout.write(f'  - {User.objects.count()} utilisateurs')
        self.stdout.write(f'  - {Client.objects.count()} clients')
        self.stdout.write(f'  - {Operation.objects.count()} opérations')
        self.stdout.write(f'  - {Notification.objects.count()} notifications')
        self.stdout.write('\nConnexions disponibles:')
        self.stdout.write('  Admin: admin / admin123')
        self.stdout.write('  Commercial 1: commercial1 / commercial123')
        self.stdout.write('  Commercial 2: commercial2 / commercial123')
