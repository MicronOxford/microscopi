  $(document).ready(function () {
    // Hide panels that should not be visible
    $('.pane-log').hide();
    $('.btn-group-view').hide();
    $('.task-status').hide();

    // Set up camera settings pane
    $.get('/api/camera/settings').then(function (r) {
      data = r['data'];

      $settings = $('#camera-settings');

      params = ['brightness', 'contrast', 'auto_exposure', 'exposure_time_absolute', 'white_balance_auto_preset', 'blue_balance', 'red_balance', 'rotate', 'horizontal_flip', 'vertical_flip', 'compression_quality'];
      params.forEach(function (param) {
        vals = data[param];
        if (vals) {
          var $input = null;
          var $label = $('<div>').html($('<label for="camera-' + param + '">' + param + '</label>'));

          if (vals['flags'] == "slider") {
            $input = $('<input id="camera-' + param + '" name="' + param + '" class="form-control" type="range" min="' + vals['min'] + '" max="' + vals['max'] + '" step="' + vals['step'] + '" placeholder="Brightness", value="' + vals['value'] + '">');
          } else if (vals['type'] == 'menu') {
            $input = $('<select id="camera-' + param + '" name="' + param + '" class="form-control" placeholder="Brightness"></select>');
            vals['menu'].forEach(function (item) {
              $option = $('<option value="' + item[0] + '">' + item[1] + '</option>');
              $input.append($option);
            })
          } else if (vals['type'] == 'bool') {
            $input = $('<select id="camera-' + param + '" name="' + param + '" class="form-control" placeholder="Brightness"></select>');
            var options = [
              [0, "Off"],
              [1, "On"]
            ];
            options.forEach(function (item) {
              $option = $('<option value="' + item[0] + '">' + item[1] + '</option>');
              $input.append($option);
            })
          } else if (vals['type'] == 'int') {
            $input = $('<input id="camera-' + param + '" name="' + param + '" class="form-control" type="range" min="' + vals['min'] + '" max="' + vals['max'] + '" step="' + vals['step'] + '" placeholder="Brightness", value="' + vals['value'] + '">');
          } else {

          }

          if ($input) {
            $settings.append($label);
            $('<div>').append($input).appendTo($settings);
            $settings.append($input);
            $input.on('change', function (e) {
              e.preventDefault();
              $el = $(e.target);
              v = $(e.target).val();
              $.get('/api/camera/settings/' + $el.attr('name') + '/' + v);
            });
          }
        }
      })

    });

    // Set up gui socket communication
    namespace = '/gui';
    socket_gui = io.connect('http://' + document.domain + ':' + location.port + namespace);

    socket_gui.on('connect', function () {
      log('/gui connected');
    });

    // Set up logging
    socket_gui.on('log', function (msg) {
      log('Received: ' + msg.data);
    });

    // Log control handlers
    $('.btn-log').on('click', function () {
      $('.pane-log').toggle();
    });

    // Focus control handlers
    $('.focus-up').on('click', function () {
      steps = parseInt($('#focus-steps').val());
      data = {
        axis: "z",
        'direction': 1,
        'steps': steps
      };
      socket_gui.emit('motor', data);
    });

    $('.focus-down').on('click', function () {
      steps = parseInt($('#focus-steps').val());
      data = {
        axis: "z",
        'direction': 0,
        'steps': steps
      }
      socket_gui.emit('motor', data);
    });

    // Stage control handlers
    $('.move-left').on('click', function () {
      steps = parseInt($('.steps').val());
      data = {
        axis: "x",
        'direction': 1,
        'steps': steps
      };
      socket_gui.emit('motor', data);
    });

    $('.move-right').on('click', function () {
      steps = parseInt($('.steps').val());
      data = {
        axis: "x",
        'direction': 0,
        'steps': steps
      }
      socket_gui.emit('motor', data);
    });

    $('.move-up').on('click', function () {
      steps = parseInt($('.steps').val());
      data = {
        axis: "y",
        'direction': 1,
        'steps': steps
      };
      socket_gui.emit('motor', data);
    });

    $('.move-down').on('click', function () {
      steps = parseInt($('.steps').val());
      data = {
        axis: "y",
        'direction': 0,
        'steps': steps
      }
      socket_gui.emit('motor', data);
    });

    // LED control handlers
    $('.btn-led-on').on('click', function () {
      data = {
        status: "on"
      };
      socket_gui.emit('led', data);
    });

    $('.btn-led-off').on('click', function () {
      data = {
        status: "off"
      };
      socket_gui.emit('led', data);
    });

    $('.btn-led-up').on('click', function () {
      data = {
        increment: 10
      };
      socket_gui.emit('ledbrightness', data);
    });

    $('.btn-led-down').on('click', function () {
      data = {
        increment: -10
      };
      socket_gui.emit('ledbrightness', data);
    });

    // Matrix control handlers
    $('.btn-matrix-on').on('click', function () {
      data = {
        status: "on"
      };
      socket_gui.emit('matrix', data);
    });

    $('.btn-matrix-off').on('click', function () {
      data = {
        status: "off"
      };
      socket_gui.emit('matrix', data);
    });

    $('.btn-matrix-up').on('click', function () {
      data = {
        increment: 1
      };
      socket_gui.emit('matrixbrightness', data);
      console.log('asdf');
    });

    $('.btn-matrix-down').on('click', function () {
      data = {
        increment: -1
      };
      socket_gui.emit('matrixbrightness', data);
    });

    $('.btn-matrix-pattern-all').on('click', function () {
      data = {
        pattern: 'all'
      };
      socket_gui.emit('matrixpattern', data);
    });

    $('.btn-matrix-pattern-none').on('click', function () {
      data = {
        pattern: 'none'
      };
      socket_gui.emit('matrixpattern', data);
    });

    $('.btn-matrix-pattern-bright').on('click', function () {
      data = {
        pattern: 'bright'
      };
      socket_gui.emit('matrixpattern', data);
    });

    $('.btn-matrix-pattern-dark').on('click', function () {
      data = {
        pattern: 'dark'
      };
      socket_gui.emit('matrixpattern', data);
    });

    $('.btn-matrix-oblique-left').on('click', function () {
      data = {
        pattern: 'left'
      };
      socket_gui.emit('matrixpattern', data);
    });

    $('.btn-matrix-oblique-right').on('click', function () {
      data = {
        pattern: 'right'
      };
      socket_gui.emit('matrixpattern', data);
    });

    $('.btn-matrix-oblique-top').on('click', function () {
      data = {
        pattern: 'top'
      };
      socket_gui.emit('matrixpattern', data);
    });

    $('.btn-matrix-oblique-bottom').on('click', function () {
      data = {
        pattern: 'bottom'
      };
      socket_gui.emit('matrixpattern', data);
    });

    // Camera and image control handlers

    $('.btn-capture').on('click', function () {
      $('.btn-group-view').hide();
      $.get('/api/camera/capture');

      $('.img-camera').animate({
          borderWidth: 8,
          opacity: 0.5
        }, 100)
        .animate({
          borderWidth: 1,
          opacity: 1
        }, 100)
    });

    $('.btn-preview').on('click', function () {
      $('.btn-group-view').hide();
      $('.move-btn').show();
      $('.img-camera').attr('src', '/camera/stream/video.mjpeg');
    });

    $('.btn-view').on('click', function () {
      $('.btn-group-view').show();
      $('.move-btn').hide();

      get_img()
        .done(function () {
          state = microscopi.state.get();
          view_img(state.images.length);
        });
    });

    $('.btn-previmage').on('click', function () {
      state = microscopi.state.get();
      if (state.curr_image > 1) {
        view_img(state.curr_image - 1);
      }
    });

    $('.btn-nextimage').on('click', function () {
      state = microscopi.state.get();
      if (state.curr_image < state.image_max) {
        view_img(state.curr_image + 1);
      }
    });

    $('.btn-saveimage').on('click', function () {
      state = microscopi.state.get();
      if (state.curr_image) {
        window.open('/api/images/' + state.curr_image + '?filename=' + state.curr_image + '.jpg', 'Download');
      }
    });

    $('.btn-deleteimage').on('click', function () {
      state = microscopi.state.get();
      if (state.curr_image) {
        $.get('/api/images/' + state.curr_image + '/delete')
          .then(function () {
            return get_img();
          })
          .then(function (data) {
            if (state.curr_image <= state.image_max) {
              view_img(state.curr_image);
            } else {
              view_img(state.image_max);
            }
          })
      }
    });

    $('.btn-timelapse').on('click', function (e) {
      e.preventDefault();
      state = microscopi.state.get();
      $.ajax({
          url: '/task/timelapse',
          method: 'POST',
          data: JSON.stringify({
            't': $('#timelapse-time').val()
          }),
          contentType: 'application/json'
        })
        .then(function (r) {})
    });

    $('.btn-zstack').on('click', function (e) {
      e.preventDefault();
      state = microscopi.state.get();
      $.ajax({
          url: '/task/zstack',
          method: 'POST',
          data: JSON.stringify({
            'n': $('#zstack-n').val(),
            'step': $('#zstack-step').val()
          }),
          contentType: 'application/json'
        })
        .then(function (r) {})
    });

    $('.btn-stitch').on('click', function (e) {
      e.preventDefault();
      state = microscopi.state.get();
      $.ajax({
          url: '/task/stitch',
          method: 'POST',
          data: JSON.stringify({
            'x_steps': $('#stitch-x').val(),
            'y_steps': $('#stitch-y').val(),
            'x_stepsize': $('#stitch-xstep').val(),
            'y_stepsize': $('#stitch-ystep').val()
          }),
          contentType: 'application/json'
        })
        .then(function (r) {})
    });

    // Set up task socket handlers
    namespace = '/task';
    socket_task = io.connect('http://' + document.domain + ':' + location.port + namespace);

    socket_task.on('connect', function () {
      log('/task connected');
    });

    socket_task.on('log', function (msg) {
      log('Received: ' + msg.data);
    });

    socket_task.on('timelapse_start', function (msg) {
      $('#timelapse-status').html('Running...').show();
    })

    socket_task.on('timelapse_end', function (msg) {
      $('#timelapse-status').html('Done');
      window.open('/timelapse', 'Download');
    })

    socket_task.on('zstack_start', function (msg) {
      $('#zstack-status').html('Running...').show();
    })

    socket_task.on('zstack_progress', function (msg) {
      $('#zstack-status').html('Running... ' + msg['curr'] + '/' + msg['max']);
    })

    socket_task.on('zstack_complete', function (msg) {
      $('#zstack-status').html('Done');
      window.open('/zstack', 'Download');
    })

    socket_task.on('stitch_start', function (msg) {
      $('#stitch-status').html('Running...').show();
    })

    socket_task.on('stitch_progress', function (msg) {
      $('#stitch-status').html('Running... x: ' + msg['curr_x'] + '/' + msg['max_x'] + '; y: ' + msg['curr_y'] + '/' + msg['max_y']);
    })

    socket_task.on('stitch_complete', function (msg) {
      $('#stitch-status').html('Done');
      window.open('/stitch', 'Download');
    })

    // Log toggle button handler
    $('#log-toggle').on('click', function (e) {
      e.preventDefault();
      $('.pane-log').toggle();
    })

    //  Functions
    function set_img(url) {
      $('.img-camera').attr('src', url + "?" + new Date().getTime());
      // ? prevents client cache
      // should set to # then disable caching on server
    }

    function get_img() {
      return $.get('/api/images').done(function (r) {
        var dfd = $.Deferred();
        microscopi.state.update({
          'images': r.data,
          'image_max': r.data.length
        });
        dfd.resolve();

        return dfd.promise();
      });
    }

    function view_img(i) {
      state = microscopi.state.get();
      if (i <= state.image_max) {
        state.curr_image = i;
        $('.img-count').html(i + '/' + state.images.length);
        set_img('/api/images/' + i);
      }
    }

    function log(msg) {
      console.log(msg);
      $('#log').append(msg + '<br/>');
    }
  });

  // Simple state module
  var microscopi = microscopi || {};
  microscopi.state = (function () {
    var state = {};

    get = function () {
      return state;
    };

    set = function (s) {
      state = s;
    };

    update = function (s) {
      $.extend(state, s);
    };

    clear = function () {
      state = {};
    };


    // Expose public
    return {
      get: get,
      set: set,
      update: update,
      clear: clear
    }

  }());