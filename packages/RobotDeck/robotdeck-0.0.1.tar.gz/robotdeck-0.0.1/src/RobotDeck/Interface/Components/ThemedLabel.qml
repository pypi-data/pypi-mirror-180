/* Base for a Dark Label

Copyright 2020 - 2021 Ant Solutions SRL (mgilles@ant-solutions.be)

*/

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

import "../Scripts/Defines.js" as Defines

Label {
   color: Defines.foregroundColor

    background: Rectangle {
        anchors.fill: parent
        color: Defines.backgroundColor
    }
}
