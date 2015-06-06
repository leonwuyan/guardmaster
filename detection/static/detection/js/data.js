(function () {
  var _askData = window.location.pathname;
  var _getCookie = function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };
  var _csrfSafeMethod = function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  };
  var _getData = function(form) {
    var tmp = {};
    $(form).each(function(idx, el) {
      if ($(el).val() != '') {
      	if ($(el).attr('type') == 'checkbox') {
      	  //first time create array
      	  if (typeof(tmp[$(el).attr('name')]) == 'undefined')
      	    tmp[$(el).attr('name')] = Array();
      	  //if input is checkbox
      	  if ($(el).prop('checked'))
      	    tmp[$(el).attr('name')].push($(el).val());
      	} else {
      	  //input isn't checkbox
      	  tmp[$(el).attr('name')] = $(el).val();
      	}
      }
    });
    return tmp;
  };
  var _addEmoji = function () {
    $('td').each(function(index, ele) {
      $(ele).emoji();
    });
  };
  var _buildTable = function(data) {
    $('#sources').dataTable({
  	'dom': 'T<"clear">lfrtip',
  	'tableTools': {
  	  'sSwfPath': '/static/detection/swf/copy_csv_xls.swf',
  	  'aButtons': [ 'csv']
  	},
  	'language': {
  	  'url': '/static/detection/js/i18n/dataTables.'+gettext('en')+'.json',
  	},
  	'ajax': {
  	  'url': _askData + '.json',
  	  'data': data
  	},
  	'autoWidth': false,
  	'scrollX': true,
  	'destroy': true,
    'order': [[0, "desc"]]
  });
    //add Emoji by every draw
    $('#sources').on('draw.dt', function () {
      _addEmoji();
    });
  };
  var _dataAccess = {
    'getJSON': function() {
      data = []
      if ($('input[name="start"]').length > 0) {
        var start = $('input[name="start"]').val();
        var end = $('input[name="end"]').val();
        if (start == '' || end == '') {
          alert('请填写起始日期和结束日期。');
          return false;
        }
        var data = '{"start":"' + start + '","end":"' + end + '"}';
        data = $.parseJSON(data);
      }
      //channel id
      var tmp = new Array();
      $('ul#channel-list li').each(function(idx, el) {
        if ($(el).hasClass('active'))
          tmp.push($(el).attr('value'));
      });
      if (tmp.length > 0) data['channel_id'] = tmp;
      tmp = new Array();
      $('ul#zone-list li').each(function(idx, el) {
        if ($(el).hasClass('active'))
          tmp.push($(el).attr('value'));
      });
      if (tmp.length > 0) data['zone_id'] = tmp;
      //end build data
      _buildTable(data);
      return false;
    },
    'onlytimeJSON': function() {
      data = []
      if ($('input[name="start"]').length > 0) {
        var start = $('input[name="start"]').val();
        var end = $('input[name="end"]').val();
        if (start == '' || end == '') {
          alert('请填写起始日期和结束日期。');
          return false;
        }
        var data = '{"start":"' + start + '","end":"' + end + '"}';
        data = $.parseJSON(data);
      }
      //end build data
      _buildTable(data);
      return false;
    },
    'withouttimeJSON': function() {
      data = []
      //channel id
      var tmp = new Array();
      $('ul#channel-list li').each(function(idx, el) {
        if ($(el).hasClass('active'))
          tmp.push($(el).attr('value'));
      });
      if (tmp.length > 0) data['channel_id'] = tmp;
      tmp = new Array();
      $('ul#zone-list li').each(function(idx, el) {
        if ($(el).hasClass('active'))
          tmp.push($(el).attr('value'));
      });
      if (tmp.length > 0) data['zone_id'] = tmp;
      //end build data
      _buildTable(data);
      return false;
    },
    'queryJSON': function() {
      var data = _getData('form#queryForm input[type="text"]');
      _buildTable(data);
      return false;
    },
    'contactJSON': function() {
      var data = _getData('form#contactForm [name]');
      _buildTable(data);
      return false;
    },
    'addJSON': function(server_id, uid, type, type_id) {
      if (uid == 0 || server_id == 0) {
        return false
      }
      var addData = {};
      var p = '';
      switch (type) {
        case 'add':
          if (!confirm(gettext('Confirm Adding 100K?'))) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'type_id': type_id,
            'uid': uid
          };
          p = '/add.json';
          break;
        case 'recharge':
          if (!confirm(gettext('Confirm Adding 10K?'))) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'uid': uid
          };
          p = '/recharge.json';
          break;
        case 'dungeon':
          fmts = gettext('Confirm Unlocking Dungeon To %(type_id)s ?');
          s = interpolate(fmts, {'type_id':type_id}, true);
          if (!confirm(s)) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'dungeon_id': type_id,
            'uid': uid
          };
          p = '/dungeon.json';
          break;
        case 'kick':
          fmts = gettext('Confirm Kicking Player UID %(uid)s ?');
          s = interpolate(fmts, {'uid':uid}, true);
          if (!confirm(s)) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'uid': uid
          };
          p = '/kick.json';
          break;
        case 'chat_ban':
          fmts = gettext('Confirm Chat Ban Player %(type_id)s Day?');
          s = interpolate(fmts, {'type_id':type_id}, true);
          if (!confirm(s)) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'time': type_id*24*60*60,
            'uid': uid
          };
          p = '/chat_ban.json';
          break;
        case 'account_ban':
          fmts = gettext('Confirm Account Ban Player %(type_id)s Day?');
          s = interpolate(fmts, {'type_id':type_id}, true);
          if (!confirm(s)) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'time': type_id*24*60*60,
            'uid': uid
          };
          p = '/account_ban.json';
          break;
      }
      $.ajax({
        url: _askData + p,
        data: addData,
        type: 'POST',
        beforeSend: function(xhr, settings) {
          if (!_csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", _getCookie('csrftoken'));
          }
        },
        success: function(msg){
          if (msg.result == '0'){
            location.reload();
            return false;
          }
          alert('Error Code : ' + msg.result);
        },
        error: function(e){
          switch (e.status) {
            case 401:
              //location.reload();
              break;
            default:
              //location.reload();
              break;
          }
        }
      });
      return false;
    }
  };
  var _queryButton = {
    'active': function(val) {
      if ($(val).length > 0) {
      	if ($(val).hasClass('active')) {
      	  $(val).removeClass('active');
      	} else {
      	  $(val).addClass('active');
      	}
      }
    },
    'initDate': function () {
      if ($('input[name="start"]').length > 0) {
      	var d = new Date();
      	var year = d.getFullYear();
      	var month = d.getMonth() + 1;
      	if (month < 10) month = '0' + month;
      	var day = d.getDate();
      	if (day < 10) day = '0' + day;
      	$('input[name="start"]').val(year + '-' + month + '-01');
      	$('input[name="end"]').val(year + '-' + month + '-' + day);
      }
      _queryButton.active('ul#zone-list li:first');
      _queryButton.active('ul#channel-list li:first');
      $('#count-button').click();
    }
  };
  var _management = {
    'numberOnly': function(obj) {
      $(obj).keyup(function(){
              $(this).val($(this).val().replace(/\D|^0/g,''));
          }).bind("paste",function(){
              $(this).val($(this).val().replace(/\D|^0/g,''));
          }).css("ime-mode", "disabled");
    },
    'addObject': function(ul, obj, count, k) {
      if ($(obj).val() == '-1') {
        return false;
      }
      if ($(count).val() == '') {
        return false;
      }
      val = $(obj).val()
      text = $(obj).find("option:selected").text()
      t = $(count).val()
      html = '<li class="list-group-item"><span class="badge">'
      html += t + '</span>'
      html += '<input name="acc" type="hidden" value="' + k + '|' + val + '|' + t + '" />'
      html += text + '</li>'
      $(ul).append(html)
    }
  };
  window.dataAccess = _dataAccess;
  window.queryButton = _queryButton;
  window.management = _management;
  window.getData = _getData;
})();
