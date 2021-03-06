# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClassifierFeature'
        db.create_table('message_classifier_classifierfeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['message_classifier.ClassifierCategory'])),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('message_classifier', ['ClassifierFeature'])

        # Adding model 'ClassifierCategory'
        db.create_table('message_classifier_classifiercategory', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['message_classifier.Department'], null=True)),
        ))
        db.send_create_signal('message_classifier', ['ClassifierCategory'])

        # Adding M2M table for field flags on 'ClassifierCategory'
        db.create_table('message_classifier_classifiercategory_flags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classifiercategory', models.ForeignKey(orm['message_classifier.classifiercategory'], null=False)),
            ('flag', models.ForeignKey(orm['contact.flag'], null=False))
        ))
        db.create_unique('message_classifier_classifiercategory_flags', ['classifiercategory_id', 'flag_id'])

        # Adding model 'ScoredMessage'
        db.create_table('message_classifier_scoredmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('trained_as', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trained_as', null=True, to=orm['message_classifier.ClassifierCategory'])),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Message'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='category', null=True, to=orm['message_classifier.ClassifierCategory'])),
        ))
        db.send_create_signal('message_classifier', ['ScoredMessage'])

        # Adding model 'Report'
        db.create_table('message_classifier_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('message_classifier', ['Report'])

        # Adding model 'Department'
        db.create_table('message_classifier_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('message_classifier', ['Department'])


    def backwards(self, orm):
        # Deleting model 'ClassifierFeature'
        db.delete_table('message_classifier_classifierfeature')

        # Deleting model 'ClassifierCategory'
        db.delete_table('message_classifier_classifiercategory')

        # Removing M2M table for field flags on 'ClassifierCategory'
        db.delete_table('message_classifier_classifiercategory_flags')

        # Deleting model 'ScoredMessage'
        db.delete_table('message_classifier_scoredmessage')

        # Deleting model 'Report'
        db.delete_table('message_classifier_report')

        # Deleting model 'Department'
        db.delete_table('message_classifier_department')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contact.flag': {
            'Meta': {'object_name': 'Flag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'rule': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'}),
            'rule_regex': ('django.db.models.fields.CharField', [], {'max_length': '700', 'null': 'True'}),
            'words': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'db.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delivered': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_response_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'responses'", 'null': 'True', 'to': "orm['db.Message']"}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Q'", 'max_length': '1', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'message_classifier.classifiercategory': {
            'Meta': {'object_name': 'ClassifierCategory'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['message_classifier.Department']", 'null': 'True'}),
            'flags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contact.Flag']", 'null': 'True', 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'})
        },
        'message_classifier.classifierfeature': {
            'Meta': {'object_name': 'ClassifierFeature'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['message_classifier.ClassifierCategory']"}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'message_classifier.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'message_classifier.report': {
            'Meta': {'object_name': 'Report'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'message_classifier.scoredmessage': {
            'Meta': {'object_name': 'ScoredMessage'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'null': 'True', 'to': "orm['message_classifier.ClassifierCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['db.Message']"}),
            'score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'trained_as': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trained_as'", 'null': 'True', 'to': "orm['message_classifier.ClassifierCategory']"})
        }
    }

    complete_apps = ['message_classifier']