from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from crm.models import Oportunidad


class Command(BaseCommand):
    help = 'Simula que las oportunidades en estado "Nuevo" tienen +7 días y las marca como "En seguimiento"'

    def handle(self, *args, **options):
        # Buscar todas las oportunidades en estado 'nuevo'
        oportunidades_nuevas = Oportunidad.objects.filter(estado='nuevo')

        count = oportunidades_nuevas.count()

        if count == 0:
            self.stdout.write("No hay oportunidades en estado 'Nuevo' para procesar.")
            return

        # Marcarlas como 'en_seguimiento' y ajustar su fecha a 8 días atrás
        ahora = timezone.now()
        for op in oportunidades_nuevas:
            op.fecha_creacion = ahora - timedelta(days=8)  # Más de 7 días
            op.estado = 'en_seguimiento'
            op.save()

        self.stdout.write(
            self.style.SUCCESS(f'Se procesaron {count} oportunidades: ahora están en "En seguimiento"')
        )