# bpmndrawio

Extract from drawio XML files containing BPMN :
- Title of the tab (Name of the process)
- Title of the swimlanes (Name of the actors)
- Title of the activity
- Relations between the activities
- Notes

-----------------
Title of the tab :
-----------------
<diagram id="5b6e1117-61cd-56dd-9d45-800471c2d4dc" name="BPMN Commande STW">

-> diagram id
-> name

-------------------------------------------
Title of the swimlanes (Name of the actors)
------------------------------------------
<mxCell id="2" value="Processus Commande cliente STORE TO WEB&lt;br&gt;" style="swimlane;html=1;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;horizontal=0;startSize=26;horizontalStack=0;labelBackgroundColor=none;strokeColor=#1C75BC;strokeWidth=2;fillColor=#ECEEF7;fontSize=12;fontColor=#1C75BC;align=center;swimlaneFillColor=#ffffff;" parent="1" vertex="1">

<mxCell id="3" value="&lt;font style=&quot;font-size: 14px&quot;&gt;Store to web&lt;br&gt;&lt;/font&gt;" style="swimlane;html=1;startSize=23;horizontal=0;fontSize=10;strokeColor=#A5BA1F;strokeWidth=2;fillColor=#E8EEAE;swimlaneFillColor=white;labelBackgroundColor=none;" parent="2" vertex="1">

-> style="swimlane;
-> value="xxxxx"; --> sometimes the name of the main swimlane (when there are sub-siwmlane)
-> parent="xx" --> to get the hierarchy

----------------------------
Title of the activity
----------------------------

<mxCell id="56cda022cb9d18e7-122" value="Sélection du produit à commander&lt;br&gt;" style="html=1;whiteSpace=wrap;rounded=1;strokeColor=#1C75BC;strokeWidth=2;fillColor=#ECEEF7;fontSize=10;spacingTop=5;" parent="3" vertex="1">

--> value="xxxxx" is filled
-> parent="xx" --> to get the hierarchy
-> activities ok
  - style="shape=ext
  - style="html=1


<mxCell id="5149ddf1a6ad4c69-120" value="5j après la &lt;br&gt;réception du colis&lt;br&gt;" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;perimeter=ellipsePerimeter;outline=standard;symbol=timer;fontSize=10;aspect=fixed;fillColor=#E8EEAE;strokeColor=#8DC63F;strokeWidth=2;" parent="3" vertex="1">

-> if value="" or (value="xx" and style="shape=mxgraph." --> it's not an activity
-> if = value= (not html) then it's not an activitvity

------------------------
relations between the activities
--------------------------------

<mxCell id="1049cc2e87a63749-161" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=1;exitY=0.5;entryX=0.5;entryY=1;jettySize=auto;orthogonalLoop=1;" parent="2" source="5149ddf1a6ad4c69-178" target="1049cc2e87a63749-158" edge="1">
        

-> source="id"
-> target="id"
-> parent="id" --> I don't care in this case
-> style="edgeStyle

----------------
Notes
---------------

style="shape=note;



---------------
Desired Output
---------------
- CSV to import in MAP

"Processus name"; 