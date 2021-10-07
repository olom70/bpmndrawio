# %%
from os import replace, truncate
from typing import Text
import xml.etree.ElementTree as ET
import re
data='''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2021-09-10T20:42:21.928Z" agent="5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/15.1.3 Chrome/89.0.4389.128 Electron/12.1.0 Safari/537.36" etag="KFTcWUJoXA6ucUvcokqC" version="15.1.3" type="device">
  <diagram id="e45bbcb4-4817-f833-fe68-a42dc8e9f8da" name="process XXXXX actuellement">
    <mxGraphModel dx="1088" dy="968" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="5b6dd56feeb6a458-1" value="Processus Vente Partenaire en version existant / cible / etape 1 de migration" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#1C75BC;strokeWidth=2;fillColor=#ECEEF7;gradientColor=none;fontSize=19;fontColor=#000000;align=center;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="40" y="40" width="880" height="40" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-2" value="&lt;div style=&quot;text-align: center ; font-size: 19px&quot;&gt;&lt;span style=&quot;font-size: 19px&quot;&gt;09/05/2018&lt;/span&gt;&lt;/div&gt;" style="rounded=0;whiteSpace=wrap;html=1;strokeColor=#1C75BC;strokeWidth=2;fillColor=#ECEEF7;gradientColor=none;fontSize=19;fontColor=#000000;align=center;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="960" y="40" width="160" height="40" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-3" value="&lt;p style=&quot;line-height: 120%&quot;&gt;Ce processus décrit les étapes de la saisie des quantités réservées pour les partenaires à leur expédition.&lt;br&gt;&lt;/p&gt;" style="text;strokeColor=#A5BA1F;fillColor=#E8EEAE;spacing=5;spacingTop=0;whiteSpace=wrap;overflow=hidden;rounded=0;fontSize=10;labelBackgroundColor=none;html=1;verticalAlign=middle;strokeWidth=2;" parent="1" vertex="1">
          <mxGeometry x="960" y="90" width="160" height="80" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-4" value="Processus Vente Partenaire" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;horizontal=0;startSize=26;horizontalStack=0;labelBackgroundColor=none;strokeColor=#1C75BC;strokeWidth=2;fillColor=#ECEEF7;fontSize=12;fontColor=#1C75BC;align=center;swimlaneFillColor=#ffffff;" parent="1" vertex="1">
          <mxGeometry x="40" y="283.5" width="1080" height="480" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-5" value="MAAT" style="swimlane;html=1;startSize=23;horizontal=0;fontSize=10;strokeColor=#A5BA1F;strokeWidth=2;fillColor=#E8EEAE;swimlaneFillColor=white;labelBackgroundColor=none;" parent="5b6dd56feeb6a458-4" vertex="1">
          <mxGeometry x="26" width="1054" height="120" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-7" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;perimeter=ellipsePerimeter;outline=standard;symbol=general;aspect=fixed;fontSize=10;fillColor=#E8EEAE;strokeColor=#8DC63F;strokeWidth=2;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="53.999999999999886" y="40" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-14" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#808285;strokeWidth=2;fontSize=10;fontColor=#8DC63F;fontStyle=1;labelBorderColor=none;" parent="5b6dd56feeb6a458-5" source="5b6dd56feeb6a458-9" target="5b6dd56feeb6a458-13" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-9" value="&lt;br&gt;L&#39;approvisionneur saisie les réservations des partenaires (1)." style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#ECEEF7;strokeColor=#1C75BC;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="131" y="20" width="90" height="80" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-13" value="Calcul des quantités ajustées (2)." style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#ECEEF7;strokeColor=#1C75BC;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="301" y="20" width="90" height="81" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontSize=10;strokeColor=#808285;fontColor=#8DC63F;fontStyle=1;labelBorderColor=none;" parent="5b6dd56feeb6a458-5" source="5b6dd56feeb6a458-7" target="5b6dd56feeb6a458-9" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="-270.5" y="16.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-23" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outlineConnect=0;outline=catching;symbol=timer;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="419" y="1" width="31" height="23" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-24" value="Toutes les nuits" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="435" y="-1" width="116" height="20" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-27" value="" style="endArrow=classic;html=1;entryX=0.5;entryY=0;exitX=0;exitY=0.5;" parent="5b6dd56feeb6a458-5" source="65696d6c7bc1525-23" target="5b6dd56feeb6a458-13" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="414" y="19.5" as="sourcePoint" />
            <mxPoint x="434" y="-13.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="384" y="6.5" />
              <mxPoint x="346" y="6.5" />
              <mxPoint x="346" y="19.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-29" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.25;entryX=0.5;entryY=1;" parent="5b6dd56feeb6a458-5" source="5b6dd56feeb6a458-13" target="65696d6c7bc1525-23" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="384" y="66.5" as="sourcePoint" />
            <mxPoint x="434" y="16.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="435" y="46.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-15" value="L&#39;approvisionneur valide l&#39;envoi des quantités partenaires (1)." style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#ECEEF7;strokeColor=#1C75BC;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="504" y="20" width="90" height="81" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-16" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;labelBackgroundColor=#ffffff;jettySize=auto;orthogonalLoop=1;strokeColor=#808285;strokeWidth=2;fontSize=10;fontColor=#8DC63F;fontStyle=1;labelBorderColor=none;" parent="5b6dd56feeb6a458-5" source="5b6dd56feeb6a458-13" target="5b6dd56feeb6a458-15" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-17" value="Envoi des ordres de transfert sur le terrain" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#ECEEF7;strokeColor=#1C75BC;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="923" y="31" width="104" height="55" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-30" value="Mode d&#39;envoi &lt;br&gt;?" style="rhombus;whiteSpace=wrap;html=1;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="622" y="29.5" width="64" height="61" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-31" value="Différé" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#ECEEF7;strokeColor=#1C75BC;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="699" y="5" width="90" height="25" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-32" value="Immédiat" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#ECEEF7;strokeColor=#1C75BC;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="699" y="89.5" width="90" height="25" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-33" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" parent="5b6dd56feeb6a458-5" source="5b6dd56feeb6a458-15" target="65696d6c7bc1525-30" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="594" y="86.5" as="sourcePoint" />
            <mxPoint x="644" y="36.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-34" value="" style="endArrow=classic;html=1;exitX=0.5;exitY=0;entryX=0;entryY=0.5;" parent="5b6dd56feeb6a458-5" source="65696d6c7bc1525-30" target="65696d6c7bc1525-31" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="634" y="36.5" as="sourcePoint" />
            <mxPoint x="684" y="-13.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="654" y="16.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-35" value="" style="endArrow=classic;html=1;exitX=0.5;exitY=1;entryX=0;entryY=0.5;" parent="5b6dd56feeb6a458-5" source="65696d6c7bc1525-30" target="65696d6c7bc1525-32" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="654" y="96.5" as="sourcePoint" />
            <mxPoint x="694" y="86.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="654" y="102.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-36" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outlineConnect=0;outline=catching;symbol=timer;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="824" y="7" width="31" height="23" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-37" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outlineConnect=0;outline=catching;symbol=timer;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="824" y="89.5" width="31" height="23" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-38" value="" style="endArrow=classic;html=1;entryX=0;entryY=0.5;" parent="5b6dd56feeb6a458-5" target="65696d6c7bc1525-36" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="789" y="17.5" as="sourcePoint" />
            <mxPoint x="844" y="-3.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-40" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" parent="5b6dd56feeb6a458-5" source="65696d6c7bc1525-32" target="65696d6c7bc1525-37" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="804" y="106.5" as="sourcePoint" />
            <mxPoint x="854" y="56.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-41" value="La nuit" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="820" y="28.5" width="41" height="20" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-42" value="Dans l&#39;heure" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="784" y="70" width="116" height="20" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-43" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=0.5;entryY=0;" parent="5b6dd56feeb6a458-5" source="65696d6c7bc1525-36" target="5b6dd56feeb6a458-17" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="874" y="46.5" as="sourcePoint" />
            <mxPoint x="924" y="-3.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="975" y="18.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-45" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;" parent="5b6dd56feeb6a458-5" source="65696d6c7bc1525-37" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="884" y="126.5" as="sourcePoint" />
            <mxPoint x="974" y="86.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="974" y="101.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="2ed5a75824c0f3d2-1" value="" style="shape=mxgraph.bpmn.user_task;html=1;outlineConnect=0;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="138" y="24.5" width="14" height="14" as="geometry" />
        </mxCell>
        <mxCell id="2ed5a75824c0f3d2-2" value="" style="shape=mxgraph.bpmn.user_task;html=1;outlineConnect=0;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="514" y="22.5" width="14" height="14" as="geometry" />
        </mxCell>
        <mxCell id="2ed5a75824c0f3d2-3" value="" style="shape=mxgraph.bpmn.service_task;html=1;outlineConnect=0;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="308" y="24.5" width="14" height="14" as="geometry" />
        </mxCell>
        <mxCell id="2ed5a75824c0f3d2-4" value="" style="shape=mxgraph.bpmn.service_task;html=1;outlineConnect=0;" parent="5b6dd56feeb6a458-5" vertex="1">
          <mxGeometry x="930" y="33.5" width="14" height="14" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-6" value="REFLEX" style="swimlane;html=1;startSize=23;horizontal=0;fontSize=10;strokeColor=#A5BA1F;strokeWidth=2;fillColor=#E8EEAE;swimlaneFillColor=white;labelBackgroundColor=none;" parent="5b6dd56feeb6a458-4" vertex="1">
          <mxGeometry x="26" y="120" width="1054" height="120" as="geometry" />
        </mxCell>
        <mxCell id="4e2ad3fcb86c6e8c-1" value="&lt;font style=&quot;font-size: 8px&quot;&gt;Préparation des ordres :&lt;br&gt;&lt;b&gt;Processus Approvisionnement aval&lt;/b&gt;&lt;/font&gt;&lt;br&gt;" style="shape=process;whiteSpace=wrap;html=1;fillColor=#e51400;strokeColor=#B20000;fontColor=#ffffff;" parent="5b6dd56feeb6a458-6" vertex="1">
          <mxGeometry x="774" y="30.5" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-17" value="NODHOS" style="swimlane;html=1;startSize=23;horizontal=0;fontSize=10;strokeColor=#A5BA1F;strokeWidth=2;fillColor=#E8EEAE;swimlaneFillColor=white;labelBackgroundColor=none;" parent="5b6dd56feeb6a458-4" vertex="1">
          <mxGeometry x="26" y="240" width="1054" height="120" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-18" value="Facturation" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#ECEEF7;strokeColor=#1C75BC;" parent="65696d6c7bc1525-17" vertex="1">
          <mxGeometry x="641" y="32.5" width="90" height="55" as="geometry" />
        </mxCell>
        <mxCell id="5b6dd56feeb6a458-8" value="Fin" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;fontSize=10;aspect=fixed;fillColor=#FCDEE0;strokeColor=#BE1E2D;strokeWidth=2;" parent="65696d6c7bc1525-17" vertex="1">
          <mxGeometry x="983.9999999999999" y="40" width="40" height="40" as="geometry" />
        </mxCell>
        <mxCell id="65696d6c7bc1525-50" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" parent="65696d6c7bc1525-17" source="65696d6c7bc1525-18" target="5b6dd56feeb6a458-8" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="784" y="76.5" as="sourcePoint" />
            <mxPoint x="834" y="26.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-47" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;" parent="5b6dd56feeb6a458-4" source="5b6dd56feeb6a458-17" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="1060" y="86.5" as="sourcePoint" />
            <mxPoint x="920" y="178.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="1070" y="58.5" />
              <mxPoint x="1070" y="116.5" />
              <mxPoint x="1070" y="180.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-49" value="" style="endArrow=classic;html=1;exitX=0;exitY=0.5;entryX=0.5;entryY=0;" parent="5b6dd56feeb6a458-4" source="4e2ad3fcb86c6e8c-1" target="65696d6c7bc1525-18" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="791" y="180.5" as="sourcePoint" />
            <mxPoint x="790" y="156.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="712" y="180.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="5070213f34c84981-1" value="BO" style="swimlane;html=1;startSize=23;horizontal=0;fontSize=10;strokeColor=#A5BA1F;strokeWidth=2;fillColor=#E8EEAE;swimlaneFillColor=white;labelBackgroundColor=none;" parent="5b6dd56feeb6a458-4" vertex="1">
          <mxGeometry x="26" y="360" width="1054" height="120" as="geometry" />
        </mxCell>
        <mxCell id="5070213f34c84981-2" value="Remontée des informations stock réservé (3)" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;fontSize=10;labelBackgroundColor=none;strokeWidth=2;fillColor=#e51400;strokeColor=#B20000;fontColor=#ffffff;" parent="5070213f34c84981-1" vertex="1">
          <mxGeometry x="641" y="40.5" width="90" height="55" as="geometry" />
        </mxCell>
        <mxCell id="5070213f34c84981-4" value="" style="endArrow=classic;html=1;exitX=1;exitY=0.5;entryX=1;entryY=0.5;fillColor=#e51400;strokeColor=#B20000;" parent="5b6dd56feeb6a458-4" source="5070213f34c84981-2" target="5b6dd56feeb6a458-8" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="810" y="436.5" as="sourcePoint" />
            <mxPoint x="1010" y="420.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="1070" y="426.5" />
              <mxPoint x="1070" y="300.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="fKQU_gtAUcq2NJ1NCJ3q-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.75;entryDx=0;entryDy=0;strokeColor=#CC0000;" parent="5b6dd56feeb6a458-4" source="5b6dd56feeb6a458-9" target="5070213f34c84981-2" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="202" y="428" />
              <mxPoint x="667" y="428" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="65696d6c7bc1525-21" value="(1) : Option de menu MAAT/Réassort &amp;amp; simulations/Besoins/Gestion du stock réservé.&lt;br&gt;(2) : Les réservations pour les partenaires ne sont pas fermes, le calcul du stock ajustée chaque nuit permet de déterminer les quantités disponibles pour les partenaires en fonction du stock disponible sur le DD et des réservations Wholesale et Web (qui sont elles, fermes et prioritaires). Traitement MAAT_NUIT_02/CALCUL_QUANTITE_AJUSTEE_XX (UC 5.10).&lt;br&gt;(3) : Ce traitement permet d&#39;alimenter à chaque chaine de nuit le BO avec les quantités réservées pour les partenaires. Traitement MAAT_NUIT_02/BO_STK_RESERV_PL.&lt;br&gt;" style="shape=note;whiteSpace=wrap;html=1;fillColor=#ffff88;strokeColor=#36393d;" parent="1" vertex="1">
          <mxGeometry x="60" y="790" width="750" height="140" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

'''
myroot = ET.fromstring(data)
cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
for mxCell in myroot.iter('mxCell'):
    try:
      cleantext = re.sub(cleanr,'', mxCell.attrib['value'])
      print(cleantext+"/"+mxCell.attrib['style'].split(';')[0])
    except:
      pass
    
# %%
tel = {'jack': '', 'sape': 4139}
if ('value' in tel):
    print(tel['value'])
if ('jack' in tel):
    print('0') if len(tel['jack']) == 0 else print(1)
tel['sape']
'value' in tel


# %%
import csv
artefactscolumns = ["key", "name", "type", "businessID", "orderNumber", "description", "serviceLevelAgreement", "frequency", "activityType", "periodicity", "platform", "contractScope"]
relationscolums = ["parentKey" ,"childKey","relationType", "metaX"]
with open('artefacts.csv', 'w+', newline='') as artefactscsvfile:
    artefactswriter = csv.writer(artefactscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    artefactswriter.writerow(artefactscolumns)


  # %%
def addt(a):
  a = a + 2
  return a

a = 1
addt(a)
print(a)


# %%
# initialise the file that will contains all the artefacts (processes & applications)
artefactscolumns = ["key", "name", "type", "businessID", "orderNumber", "description", "serviceLevelAgreement", "frequency", "activityType", "periodicity", "platform", "contractScope"]
with open('artefacts.csv', 'w+', newline='') as artefactscsvfile:
    artefactswriter = csv.writer(artefactscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

# initialise the file that will contains all the relations (processes & applications)
relationscolumns = ["parentKey" ,"childKey","relationType", "metaX"]
with open('relations.csv', 'w+', newline='') as relationscsvfile:
    relationswriter = csv.writer(relationscsvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

def writecsv():
    artefactswriter.writerow(artefactscolumns)
    relationswriter.writerow(relationscolumns)

writecsv()
# %%
file = 'Vendre - Ventes Wholesales & Partenaires BPMN Commande web DW avec OMS (1)-process commande web sous Demandware.drawio.xml'
filename = file[file.rfind('-')+1:-(len(file)-(file.find('.')))]
print(filename)
# %%
v = 'a'
listt = ['a', 'b', 'c']
'd' in listt
# %%
not ('aa' == 'bb')
# %%
var = [0, 1]
varb = var

varb[0] = 2
print(var)
# %%
import csv
def createfile(l):
  r = []
  for v in l:
    csvfile = open(v, 'w+', newline='')
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    r += [csvfile, writer]
  return r

w = createfile(['names3.csv', 'names4.csv'])
print(w)
w[1].writeheader()
w[1].writerow({'first_name': 'Baked', 'last_name': 'Beans'})
w[1].writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
w[1].writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
w[3].writeheader()
w[3].writerow({'first_name': 'Baked', 'last_name': 'Beans'})
w[3].writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
w[3].writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
w[0].close()
w[2].close()
# %%
a = []
a = a + [1, 0]
a = a + [2, 3]
print(a)
# %%
import pylightxl as xl
db = xl.readxl(fn='C:/work/EDL.xlsx')
db.ws_names
spheresNames = db.ws(ws='Sphere').col(col=1)
spheresDescription = db.ws(ws='Sphere').col(col=2)
for items in zip(spheresNames, spheresDescription):
  print('name : {name}, desc : {desc}'.format(name=items[0], desc=items[1]))

# %%
import re
cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def cleanName(value: str, trimSpace=False, removeDiacritic=False, changeCase=['uppercase', 'lowercase', 'noChange']):
    '''
        remove specials characters, html elements.
        also remove spaces and diacritics if asked to do
    '''
    diacritics = {'à': 'a', 'â': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'ç': 'c', 'ô': 'o', 'ö': 'o', 'ù': 'u'}
   
    def rd(v):
        cleanstr = ''
        for i, char in enumerate(v):
            if char in diacritics:
                cleanstr = cleanstr + diacritics[char] 
            else:
                cleanstr = cleanstr + v[i] 
        return cleanstr

    if trimSpace: c = re.sub(cleanr,'', value).replace(" ", "")
    if not trimSpace: c = re.sub(cleanr,'', value)
    if removeDiacritic: c = rd(c)    
    if changeCase == 'uppercase': c = c.upper()
    if changeCase == 'lowercase': c = c.lower()
    if len(c) == 0: c = 'NoName'
    return c


v = 'é a bonjour è '
print(cleanName(v, True,True, 'lowercase'))

# %%
v = 'é a bonjour è '
diacritics = {'à': 'a', 'â': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'ç': 'c', 'ô': 'o', 'ö': 'o', 'ù': 'u'}
cleanstr = ''
for i, char in enumerate(v):
    if char in diacritics:
      cleanstr = cleanstr + diacritics[char] 
    else:
      cleanstr = cleanstr + v[i] 
print(cleanstr)

# %%
diacritics = {'à': 'a', 'â': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'ç': 'c', 'ô': 'o', 'ö': 'o', 'ù': 'u'}
'à' in diacritics
# %%
PROJECT_ID = 'storied-chariot-328315'
def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

translate_text('fr', 'hello')
# %%
import lib.stringutil as stringutil
v=''' dfdf\n fdf\nf
'''
c = stringutil.cleanName(v, False, False, 'noChange', True)
print(c)
# %%
import lib.stringutil as stringutil
v=''' dfdf\n fdf\nf
'''
print(v.replace("\n", ''))
# %%
