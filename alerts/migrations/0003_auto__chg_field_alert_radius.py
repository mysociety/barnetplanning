# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Alert.radius'
        db.alter_column('alerts_alert', 'radius', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'Alert.radius'
        db.alter_column('alerts_alert', 'radius', self.gf('django.db.models.fields.IntegerField')())
    
    
    models = {
        'alerts.alert': {
            'Meta': {'object_name': 'Alert'},
            'applications': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['applications.Application']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'radius': ('django.db.models.fields.IntegerField', [], {'default': '800', 'null': 'True', 'blank': 'True'}),
            'ward_mapit_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'applications.application': {
            'Meta': {'object_name': 'Application'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'council_reference': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_url': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'received': ('django.db.models.fields.DateField', [], {}),
            'ward_mapit_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'emailconfirmation.emailconfirmation': {
            'Meta': {'object_name': 'EmailConfirmation'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'page_after': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['alerts']
