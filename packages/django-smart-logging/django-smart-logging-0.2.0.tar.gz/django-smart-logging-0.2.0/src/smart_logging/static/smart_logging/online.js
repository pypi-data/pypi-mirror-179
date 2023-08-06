(function ($) {
    $(function () {
        let selectLevel = $("select[name=level]");
        let searchInput = $("input[type=text][class=search]");
        let targetTable = $("table.filtered.online tbody");
        let targetRows = $("table.filtered.online tr:not('.header')");
        let lastData = [];

        function hash(log) {
            var _hash = 0;
            var string, x;
            let fields = ["created", "levelname", "name", "msg"];
            for (x in fields) {
                string = log[fields[x]];
                if (string.length === 0) {
                    continue;
                }
                for (i = 0; i < string.length; i++) {
                    ch = string.charCodeAt(i);
                    _hash = ((_hash << 5) - _hash) + ch;
                    _hash = _hash & _hash;
                }
            }
            return _hash;
        }

        function delay(callback, ms) {
            var timer = 0;
            return function () {
                var context = this, args = arguments;
                clearTimeout(timer);
                timer = setTimeout(function () {
                    callback.apply(context, args);
                }, ms || 0);
            };
        }

        function filterTable() {
            var level = selectLevel.val();
            var searchText = (searchInput.val() || "").toUpperCase();
            if (level || searchText) {
                targetRows.each(function (i, el) {
                    var visible = true;
                    if (level) {
                        var label = selectLevel.find("option:selected").text();
                        let rowLevel = $(el).find("td.level").text();
                        visible = visible && rowLevel === label;
                    }

                    if (searchText && visible) {
                        let rowLogger = $(el).find("td.search").text().toUpperCase();
                        visible = visible && (rowLogger.toUpperCase().indexOf(searchText) > -1);
                    }
                    if (visible) {
                        $(el).show();
                    } else {
                        $(el).hide();
                    }
                });
            } else {
                $("table.filtered tr:not('.header')").show();
            }
        }

        selectLevel.on("change", filterTable);
        searchInput.on("keyup", delay(filterTable));
        $("#clear").on("click", function () {
            console.log("Clearing logs");
            $.ajax({
                url: "./?page=clear", success: function () {
                    fetch();
                }
            });
        });

        function fetch() {
            console.log("Fetching logs");
            $.ajax({
                url: "./?page=logs",
                method: "GET",
                success: function (data) {
                    targetTable.html("");
                    fetchData = [];
                    $(data).each(function (index, item) {
                        var h = hash(item);
                        var cls = lastData.indexOf(h) >=0 ? "": "new";
                        fetchData.push(h)
                        targetTable.prepend(
                            "<tr class='" + cls +"'><td class='rownum'>" + (index + 1) +
                            "</td><td class='timestamp'>" + item.created +
                            "</td><td>" + item.levelname +
                            "</td><td>" + item.name +
                            "</td><td>" + item.msg +
                            "</td></tr>"
                        );
                    });
                    lastData = fetchData;
                }
            });
        }

        setInterval(fetch, 5000);
        filterTable();
        fetch();
    });
})($);
