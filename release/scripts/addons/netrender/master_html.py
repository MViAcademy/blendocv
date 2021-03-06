# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import os
import shutil
from netrender.utils import *
import netrender.model

src_folder = os.path.split(__file__)[0]

def get(handler):
    def output(text):
        handler.wfile.write(bytes(text, encoding='utf8'))

    def head(title, refresh = False):
        output("<html><head>")
        if refresh:
            output("<meta http-equiv='refresh' content=5>")
        output("<script src='/html/netrender.js' type='text/javascript'></script>")
#		output("<script src='/html/json2.js' type='text/javascript'></script>")
        output("<title>")
        output(title)
        output("</title></head><body>")
        output("<link rel='stylesheet' href='/html/netrender.css' type='text/css'>")


    def link(text, url, script=""):
        return "<a href='%s' %s>%s</a>" % (url, script, text)

    def tag(name, text, attr=""):
        return "<%s %s>%s</%s>" % (name, attr, text, name)

    def startTable(border=1, class_style = None, caption = None):
        output("<table border='%i'" % border)

        if class_style:
            output(" class='%s'" % class_style)

        output(">")

        if caption:
            output("<caption>%s</caption>" % caption)

    def headerTable(*headers):
        output("<thead><tr>")

        for c in headers:
            output("<td>" + c + "</td>")

        output("</tr></thead>")

    def rowTable(*data, id = None, class_style = None, extra = None):
        output("<tr")

        if id:
            output(" id='%s'" % id)

        if class_style:
            output(" class='%s'" % class_style)

        if extra:
            output(" %s" % extra)

        output(">")

        for c in data:
            output("<td>" + str(c) + "</td>")

        output("</tr>")

    def endTable():
        output("</table>")

    def checkbox(title, value, script=""):
        return """<input type="checkbox" title="%s" %s %s>""" % (title, "checked" if value else "", ("onclick=\"%s\"" % script) if script else "")

    if handler.path == "/html/netrender.js":
        f = open(os.path.join(src_folder, "netrender.js"), 'rb')

        handler.send_head(content = "text/javascript")
        shutil.copyfileobj(f, handler.wfile)

        f.close()
    elif handler.path == "/html/netrender.css":
        f = open(os.path.join(src_folder, "netrender.css"), 'rb')

        handler.send_head(content = "text/css")
        shutil.copyfileobj(f, handler.wfile)

        f.close()
    elif handler.path == "/html" or handler.path == "/":
        handler.send_head(content = "text/html")
        head("NetRender", refresh = True)

        output("<h2>Jobs</h2>")

        startTable()
        headerTable(
                        "&nbsp;",
                        "id",
                        "name",
                        "category",
                        "type",
                        "chunks",
                        "priority",
                        "usage",
                        "wait",
                        "status",
                        "length",
                        "done",
                        "dispatched",
                        "error",
                        "priority",
                        "exception"
                    )

        handler.server.balance()

        for job in handler.server.jobs:
            results = job.framesStatus()
            rowTable(
                        """<button title="cancel job" onclick="cancel_job('%s');">X</button>""" % job.id +
                        """<button title="pause job" onclick="request('/pause_%s', null);">P</button>""" % job.id +
                        """<button title="reset all frames" onclick="request('/resetall_%s_0', null);">R</button>""" % job.id,
                        job.id,
                        link(job.name, "/html/job" + job.id),
                        job.category if job.category else "<i>None</i>",
                        netrender.model.JOB_TYPES[job.type],
                        str(job.chunks) +
                        """<button title="increase chunks size" onclick="request('/edit_%s', &quot;{'chunks': %i}&quot;);">+</button>""" % (job.id, job.chunks + 1) +
                        """<button title="decrease chunks size" onclick="request('/edit_%s', &quot;{'chunks': %i}&quot;);" %s>-</button>""" % (job.id, job.chunks - 1, "disabled=True" if job.chunks == 1 else ""),
                        str(job.priority) +
                        """<button title="increase priority" onclick="request('/edit_%s', &quot;{'priority': %i}&quot;);">+</button>""" % (job.id, job.priority + 1) +
                        """<button title="decrease priority" onclick="request('/edit_%s', &quot;{'priority': %i}&quot;);" %s>-</button>""" % (job.id, job.priority - 1, "disabled=True" if job.priority == 1 else ""),
                        "%0.1f%%" % (job.usage * 100),
                        "%is" % int(time.time() - job.last_dispatched),
                        job.statusText(),
                        len(job),
                        results[DONE],
                        results[DISPATCHED],
                        str(results[ERROR]) +
                        """<button title="reset error frames" onclick="request('/reset_%s_0', null);" %s>R</button>""" % (job.id, "disabled=True" if not results[ERROR] else ""),
                        "yes" if handler.server.balancer.applyPriorities(job) else "no",
                        "yes" if handler.server.balancer.applyExceptions(job) else "no"
                    )

        endTable()
        
        output("<h2>Slaves</h2>")

        startTable()
        headerTable("name", "address", "last seen", "stats", "job")

        for slave in handler.server.slaves:
            rowTable(slave.name, slave.address[0], time.ctime(slave.last_seen), slave.stats, link(slave.job.name, "/html/job" + slave.job.id) if slave.job else "None")

        endTable()

        output("<h2>Configuration</h2>")

        output("""<button title="remove all jobs" onclick="clear_jobs();">CLEAR JOB LIST</button>""")

        startTable(caption = "Rules", class_style = "rules")

        headerTable("type", "enabled", "description", "limit")

        for rule in handler.server.balancer.rules:
            rowTable(
                        "rating",
                        checkbox("", rule.enabled, "balance_enable('%s', '%s')" % (rule.id(), str(not rule.enabled).lower())),
                        rule,
                        rule.str_limit() +
                        """<button title="edit limit" onclick="balance_edit('%s', '%s');">edit</button>""" % (rule.id(), str(rule.limit)) if hasattr(rule, "limit") else "&nbsp;"
                    )

        for rule in handler.server.balancer.priorities:
            rowTable(
                        "priority",
                        checkbox("", rule.enabled, "balance_enable('%s', '%s')" % (rule.id(), str(not rule.enabled).lower())),
                        rule,
                        rule.str_limit() +
                        """<button title="edit limit" onclick="balance_edit('%s', '%s');">edit</button>""" % (rule.id(), str(rule.limit)) if hasattr(rule, "limit") else "&nbsp;"
                    )

        for rule in handler.server.balancer.exceptions:
            rowTable(
                        "exception",
                        checkbox("", rule.enabled, "balance_enable('%s', '%s')" % (rule.id(), str(not rule.enabled).lower())),
                        rule,
                        rule.str_limit() +
                        """<button title="edit limit" onclick="balance_edit('%s', '%s');">edit</button>""" % (rule.id(), str(rule.limit)) if hasattr(rule, "limit") else "&nbsp;"
                    )

        endTable()

        output("</body></html>")

    elif handler.path.startswith("/html/job"):
        handler.send_head(content = "text/html")
        job_id = handler.path[9:]

        head("NetRender")

        job = handler.server.getJobID(job_id)

        if job:
            output("<h2>Render Information</h2>")

            job.initInfo()

            startTable()

            rowTable("resolution", "%ix%i at %i%%" % job.resolution)

            endTable()


            if job.type == netrender.model.JOB_BLENDER:
                output("<h2>Files</h2>")
                
                startTable()
                headerTable("path")
    
                tot_cache = 0
                tot_fluid = 0
    
                rowTable(job.files[0].filepath)
                rowTable("Other Files", class_style = "toggle", extra = "onclick='toggleDisplay(&quot;.other&quot;, &quot;none&quot;, &quot;table-row&quot;)'")
    
                for file in job.files:
                    if file.filepath.endswith(".bphys"):
                        tot_cache += 1
                    elif file.filepath.endswith(".bobj.gz") or file.filepath.endswith(".bvel.gz"):
                        tot_fluid += 1
                    else:
                        if file != job.files[0]:
                            rowTable(file.filepath, class_style = "other")
    
                if tot_cache > 0:
                    rowTable("%i physic cache files" % tot_cache, class_style = "toggle", extra = "onclick='toggleDisplay(&quot;.cache&quot;, &quot;none&quot;, &quot;table-row&quot;)'")
                    for file in job.files:
                        if file.filepath.endswith(".bphys"):
                            rowTable(os.path.split(file.filepath)[1], class_style = "cache")
    
                if tot_fluid > 0:
                    rowTable("%i fluid bake files" % tot_fluid, class_style = "toggle", extra = "onclick='toggleDisplay(&quot;.fluid&quot;, &quot;none&quot;, &quot;table-row&quot;)'")
                    for file in job.files:
                        if file.filepath.endswith(".bobj.gz") or file.filepath.endswith(".bvel.gz"):
                            rowTable(os.path.split(file.filepath)[1], class_style = "fluid")
    
                endTable()
            elif job.type == netrender.model.JOB_VCS:
                output("<h2>Versioning</h2>")
                
                startTable()
    
                rowTable("System", job.version_info.system.name)
                rowTable("Remote Path", job.version_info.rpath)
                rowTable("Working Path", job.version_info.wpath)
                rowTable("Revision", job.version_info.revision)
                rowTable("Render File", job.files[0].filepath)
    
                endTable()

            if job.blacklist:
                output("<h2>Blacklist</h2>")

                startTable()
                headerTable("name", "address")

                for slave_id in job.blacklist:
                    slave = handler.server.slaves_map.get(slave_id, None)
                    if slave:
                        rowTable(slave.name, slave.address[0])

                endTable()

            output("<h2>Frames</h2>")

            startTable()
            headerTable("no", "status", "render time", "slave", "log", "result", "")

            for frame in job.frames:
                rowTable(
                         frame.number,
                         frame.statusText(),
                         "%.1fs" % frame.time,
                         frame.slave.name if frame.slave else "&nbsp;",
                         link("view log", logURL(job_id, frame.number)) if frame.log_path else "&nbsp;",
                         link("view result", renderURL(job_id, frame.number))  + " [" +
                         tag("span", "show", attr="class='thumb' onclick='showThumb(%s, %i)'" % (job.id, frame.number)) + "]" if frame.status == DONE else "&nbsp;",
                         "<img name='thumb%i' title='hide thumbnails' src='' class='thumb' onclick='showThumb(%s, %i)'>" % (frame.number, job.id, frame.number)
                         )

            endTable()
        else:
            output("no such job")

        output("</body></html>")

