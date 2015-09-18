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
  var _getTime = function (t) {
    var d = new Date();
    var year = d.getFullYear();
    var month = d.getMonth() + 1;
    if (month < 10) month = '0' + month;
    var day = d.getDate();
    if (day < 10) day = '0' + day;
    var hour = d.getHours();
    if (hour < 10) hour = '0' + hour;
    var minute = d.getMinutes();
    if (minute < 10) minute = '0' + minute;
    var second = d.getSeconds();
    if (second < 10) second = '0' + second;
    date = year + '-' + month + '-' + day
    time = hour + ':' + minute + ':' + second
    if (t){
      return date + ' ' + time
    } else {
      return date
    }
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
      if ($('input[name="start"]').length > 0) {
        var start = $('input[name="start"]').val();
        var end = $('input[name="end"]').val();
        if (start == '' || end == '') {
          alert('请填写起始日期和结束日期。');
          return false;
        }
      }
      var data = _getData('form#queryForm [name]');
      _buildTable(data);
      return false;
    },
    'history_queryJSON': function() {
      if ($('input[name="start"]').length > 0) {
        var start = $('input[name="start"]').val();
        var end = $('input[name="end"]').val();
        if (start == '' || end == '') {
          alert('请填写起始日期和结束日期。');
          return false;
        }
        if (start > end) {
          alert('起始日期请小于结束日期');
          return false;
        }
        var start_date = new Date(Date.parse(start.replace(/-/g, "/")));
        var end_date = new Date(Date.parse(end.replace(/-/g, "/")));
        s_d = start_date.getDate();
        e_d = end_date.getDate();
        if (end_date.getHours() == 0 && end_date.getMinutes() == 0 && end_date.getSeconds() == 0){
          e_d -= 1;
        }
        if (s_d != e_d){
          alert('日期范围请在一个自然天')
          return false;
        }
        if ($('#uid').val() == ''){
          alert('请输入玩家ID');
          return false;
        }
      }
      var data = _getData('form#queryForm [name]');
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
          iname = type + type_id;
          count = $('input[name='+iname+']').val() || 100000;
          $('input[name='+iname+']').val(count);
          fmts = gettext('Confirm Adding %(count)s ?');
          s = interpolate(fmts, {'count':count}, true);
          if (!confirm(s)) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'type_id': type_id,
            'count': count,
            'uid': uid
          };
          p = '/add.json';
          break;
        case 'recharge':
          iname = type + type_id;
          count = $('input[name='+iname+']').val() || 10000;
          $('input[name='+iname+']').val(count);
          fmts = gettext('Confirm Change To %(count)s ?');
          s = interpolate(fmts, {'count':count}, true);
          if (!confirm(s)) {
            return false;
          }
          addData = {
            'server_id': server_id,
            'count': count,
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
    },
    'notifyJSON': function(id, title) {
      fmts = gettext('Confirm To Delete This Notify %(title)s?');
      s = interpolate(fmts, {'title':title}, true);
      if (!confirm(s)) {
        return false;
      }
      _url = _askData.substring(0, _askData.lastIndexOf('/')) + '/' + id
      $.ajax({
        url: _url,
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
          alert('Page Error Code : ' + e.status);
        }
      });
      return false;
    },
    'synchronization': function() {
      s = gettext('Confirm To Synchronize All The Noitfy To The CDNServer?');
      if (!confirm(s)) {
        return false;
      }
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
      	var month_start = d.getMonth();
        if (month_start == 0) {
          month_start = 12;
          year -= 1;
        }
        var month_end = d.getMonth() + 1;
        if (month_start < 10) month_start = '0' + month_start;
        if (month_end < 10) month_end = '0' + month_end;
      	var day = d.getDate();
      	if (day < 10) day = '0' + day;
      	$('input[name="start"]').val(year + '-' + '06-27');
      	$('input[name="end"]').val(year + '-' + month_end + '-' + day);
      }
      _queryButton.active('ul#zone-list li:first');
      _queryButton.active('ul#channel-list li:first');
      $('#count-button').click();
    },
    'initQuery': function () {
      if ($('input[name="start"]').length > 0) {
        time = _getTime(false);
        $('input[name="start"]').val(time);
        $('input[name="end"]').val(time);
      }
    },
    'initHistoryQuery': function () {
      if ($('input[name="start"]').length > 0) {
        end_time = _getTime(true);
        start_time = end_time.replace(/ (\w+):(\w+):(\w+)/, " 00:00:00");
        $('input[name="start"]').val(start_time);
        $('input[name="end"]').val(end_time);
      }
    },
    'initEveryDayHistoryQuery': function () {
      if ($('input[name="start"]').length > 0) {
        end_time = _getTime(true);
        start_time = end_time.replace(/ (\w+):(\w+):(\w+)/, " 00:00:00");
        $('input[name="start"]').val(start_time);
        $('input[name="end"]').val(start_time);
      }
    },
    'mailConfirm': function () {
      if ($('#title').val() == "" || $('#content').val() == ""){
        alert(gettext('Title And Content Is Required'));
        return false;
      }
      fmts = gettext('Please Confirm This:\nTitle :%(t)s\nContent :%(c)s');
      s = interpolate(fmts, {'t':$('#title').val(), 'c':$('#content').val()}, true);
      if (!confirm(s)) {
        return false;
      }
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
      exp = 0
      level = 0
      growup = 0
      if(count == '#equip-count'){
        exp = $('#equip-exp').val()
        level = $('#equip-level').val()
        growup = $('#equip-growup').val()
        if(exp == '') exp = 0
        if(level == '') level = 0
        if(growup == '') growup = 0
        text += ' [ ' + exp + ' | ' + level + ' | ' + growup + ' ]'
      }
      html = '<li class="list-group-item"><span class="badge">'
      html += t + '</span>'
      html += '<input name="acc" type="hidden" value="' + k + '|' + val + '|' + t + '|' + exp + '|' + level + '|' + growup + '" />'
      html += text + '</li>'
      $(ul).append(html)
    }
  };
  var _deployment = {
    'last_version': function(hostname, platform, channel, inherit, i) {
      url = window.location.pathname
      url_arr = url.split("/", 3).concat([hostname, platform, channel])
      url = url_arr.join("/") + '/upload.json'
      $.ajax({
        url: url,
        type: 'GET',
        success: function(msg){
          $('#'+ inherit +'a').val(msg.a);
          $('#'+ inherit +'b').val(msg.b);
          $('#'+ inherit +'c').val(msg.c);
          url = window.location.pathname;
          if (url.lastIndexOf("app") < 0) {
            $('#'+ inherit +'d').val(parseInt(msg.d) + i);
          }
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
    },
    'patchUploadConfirm': function() {
      fmts = gettext('Please Confirm This:\nHostName :%(h)s\nPlatform :%(p)s\nChannel :%(c)s\nVerseion :%(v)s');
      t = {
        'h':$('#hostname').val(),
        'p':$('#platform').val(),
        'c':$('#channel').val(),
        'v':$('#a').val() + '.' + $('#b').val() + '.' + $('#c').val() + '.' + $('#d').val()
      }
      s = interpolate(fmts, t, true);
      if (!confirm(s)) {
        return false;
      }
    }
  };
  window.dataAccess = _dataAccess;
  window.queryButton = _queryButton;
  window.management = _management;
  window.deployment = _deployment;
  window.getData = _getData;
  window.getTime = _getTime;
})();
