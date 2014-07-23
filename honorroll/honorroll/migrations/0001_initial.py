# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table(u'honorroll_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'honorroll', ['Organization'])

        # Adding model 'Honoree'
        db.create_table(u'honorroll_honoree', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('affiliation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['honorroll.Organization'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'honorroll', ['Honoree'])

        # Adding model 'Honor'
        db.create_table(u'honorroll_honor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('award_level', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bar_status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('honoree', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['honorroll.Honoree'])),
        ))
        db.send_create_signal(u'honorroll', ['Honor'])


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table(u'honorroll_organization')

        # Deleting model 'Honoree'
        db.delete_table(u'honorroll_honoree')

        # Deleting model 'Honor'
        db.delete_table(u'honorroll_honor')


    models = {
        u'honorroll.honor': {
            'Meta': {'object_name': 'Honor'},
            'award_level': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bar_status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'honoree': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['honorroll.Honoree']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'honorroll.honoree': {
            'Meta': {'object_name': 'Honoree'},
            'affiliation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['honorroll.Organization']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'honorroll.organization': {
            'Meta': {'object_name': 'Organization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['honorroll']