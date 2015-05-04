(function () {
  var _askData = window.location.pathname;
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
  var _getPermission = function (modal) {
    var tmp = {};
    tmp['permission'] = Array();
    $(modal).each(function(idx, el) {
      if ($(el).attr('role') == 'permission') {
        if ($(el).hasClass('active')) {
          tmp['permission'].push($(el).attr('value'));
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
  	'destroy': true
  });
    //add Emoji by every draw
    $('#sources').on('draw.dt', function () {
      _addEmoji();
    });
  };
  var _dataAccess = {
    'getJSON': function() {
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
      //if ($('#37').hasClass('active')) data['channelid'] = ['37'];
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
      //theme value
      if ($('#theme').length > 0)
	      if ($('#theme').val().length > 0) data['theme'] = $('#theme').val();
      //end build data
      _buildTable(data);
      return false;
    },
    'queryJSON': function() {
      var data = _getData('form#queryForm input[type="text"]');
      _buildTable(data);
      return false;
    },
    'createEmail': function() {
      var emailData = _getData('form [name]');
      $.ajax({
	url: '/update/' + _askData,
	data: emailData,
	type: 'POST',
	success: function(msg){
	  alert( "Data Saved: " + msg );
	},
	error: function(e){
	  switch (e.status) {
	    case 401:
	      location.reload();
	      break;
	    default:
	      alert( "添加失败，请检查输入内容" );
	      $('button.close').click();
	      break;
	  }
	}
      });
    },
    'createNotify': function() {
      var notifyData = _getData('form#notifyform [name]');
      $.ajax({
	url: '/update/' + _askData,
	data: notifyData,
	type: 'POST',
	success: function(msg){
	  alert( "添加成功" );
	  $('button.close').click();
	  location.reload();
	},
	error: function(e){
	  switch (e.status) {
	    case 401:
	      location.reload();
	      break;
	    case 405:
	      alert( "插入数据库失败，请联系管理员" );
	      $('button.close').click();
	      break;
	    default:
	      alert( "添加失败，请检查输入内容" );
	      break;
	  }
	}
      });
    },
    'updatePermission': function() {
      var permissionData = _getPermission('form [role]');
      permissionData['userID'] = window.user_id;
      $.ajax({
        url: '/update/' + _askData,
        data: permissionData,
        type: 'POST',
        success: function(msg){
          alert( "更新权限成功！" );
          $('#permissionList').modal('hide');
          location.reload();
        },
        error: function(e){
	  switch (e.status) {
	    case 401:
	      location.reload();
	      break;
	    default:
	      alert( "更新失败" );
	      $('button.close').click();
	      break;
	  }
        }
      });
    },
    'sendButton': function(){
      var str = "确定需要分发所有待发布的公告?";
      var cannelstr = "取消了分发操作";
      if (confirm(str)) {
	$.ajax({
          url: '/update/' + 'send' + _askData,
          type: 'POST',
          success: function(msg){
            alert("分发成功！");
	    //console.log(msg);
            location.reload();
          },
          error: function(e){
	    switch (e.status) {
	      case 401:
		location.reload();
		break;
	      default:
		alert( "分发失败，请删除不合法的待发布公告，谢谢。" );
		break;
	    }
          }
	});
      } else {
	console.log(cannelstr);
      }
    },
    'deleteButton': function(p) {
      var id = p;
      var str = "确定需要删除ID为" + id + "的内容?如果此公告已经分发过，则会撤回在对应游戏服务器上面的公告内容";
      var cannelstr = "取消了删除ID为" + id + "内容的操作";
      if (confirm(str)) {
	var deleteData = {};
	deleteData['NotifyID'] = id;
	$.ajax({
          url: '/update/' + 'delete' + _askData,
          data: deleteData,
          type: 'POST',
          success: function(msg){
            alert( "删除成功！" );
	    //console.log(msg);
            location.reload();
          },
          error: function(e){
	    switch (e.status) {
	      case 401:
		location.reload();
		break;
	    default:
		alert( "删除失败" );
		break;
	    }
          }
	});
      } else {
	console.log(cannelstr);
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
    'initPermission': function() {
      _buildTable();
    }
  };
  window.dataAccess = _dataAccess;
  window.queryButton = _queryButton;
  window.management = _management;
})();
