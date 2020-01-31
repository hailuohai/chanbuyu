
from django.db import models



class Club(models.Model):
    time = models.FloatField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    fee_long = models.FloatField(db_column='FEE_LONG', blank=True, null=True)  # Field name made lowercase.
    fee_short = models.FloatField(db_column='FEE_SHORT', blank=True, null=True)  # Field name made lowercase.
    hedge_okex = models.FloatField(db_column='HEDGE_OKEX', blank=True, null=True)  # Field name made lowercase.
    hedge_bitmex = models.FloatField(db_column='HEDGE_BITMEX', blank=True, null=True)  # Field name made lowercase.
    option_okex = models.FloatField(db_column='OPTION_OKEX', blank=True, null=True)  # Field name made lowercase.
