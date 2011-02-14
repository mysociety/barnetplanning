# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'StaticText'
        db.create_table('static_texts_statictext', (
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('static_texts', ['StaticText'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'StaticText'
        db.delete_table('static_texts_statictext')
    
    
    models = {
        'static_texts.statictext': {
            'Meta': {'object_name': 'StaticText'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }
    
    complete_apps = ['static_texts']
