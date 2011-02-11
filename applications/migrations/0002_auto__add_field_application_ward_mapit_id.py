# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Application.ward_mapit_id'
        db.add_column('applications_application', 'ward_mapit_id', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Application.ward_mapit_id'
        db.delete_column('applications_application', 'ward_mapit_id')
    
    
    models = {
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
        }
    }
    
    complete_apps = ['applications']
