# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('bees_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('bees', ['Category'])

        # Adding model 'Event'
        db.create_table('bees_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bees.Category'], null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('preview_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['daguerre.Image'], null=True, blank=True)),
            ('media_gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bees.Gallery'], null=True, blank=True)),
        ))
        db.send_create_signal('bees', ['Event'])

        # Adding model 'Gallery'
        db.create_table('bees_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('index', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('bees', ['Gallery'])

        # Adding model 'Photo'
        db.create_table('bees_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['daguerre.Image'])),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['bees.Gallery'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
        ))
        db.send_create_signal('bees', ['Photo'])

        # Adding model 'Member'
        db.create_table('bees_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=40)),
            ('current_member', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('grad_year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('titles', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('weapon', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['daguerre.Image'], null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bees', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('bees_category')

        # Deleting model 'Event'
        db.delete_table('bees_event')

        # Deleting model 'Gallery'
        db.delete_table('bees_gallery')

        # Deleting model 'Photo'
        db.delete_table('bees_photo')

        # Deleting model 'Member'
        db.delete_table('bees_member')


    models = {
        'bees.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'bees.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bees.Category']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'media_gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bees.Gallery']", 'null': 'True', 'blank': 'True'}),
            'preview_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['daguerre.Image']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'bees.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bees.member': {
            'Meta': {'object_name': 'Member'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'current_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['daguerre.Image']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weapon': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'bees.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['bees.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['daguerre.Image']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        },
        'daguerre.image': {
            'Meta': {'object_name': 'Image'},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['bees']