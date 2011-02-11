# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Application'
        db.create_table('applications_application', (
            ('received', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('info_url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('council_reference', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('applications', ['Application'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Application'
        db.delete_table('applications_application')
    
    
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
            'received': ('django.db.models.fields.DateField', [], {})
        }
    }
    
    complete_apps = ['applications']
