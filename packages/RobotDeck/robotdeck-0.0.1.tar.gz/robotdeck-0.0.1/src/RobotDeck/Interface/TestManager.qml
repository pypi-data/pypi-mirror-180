/* Test Manager is the main Module for Robot Deck, allows to manage projects and tests.

Copyright 2020 - 2021 Ant Solutions SRL (info@ant-solutions.be)

*/

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

import "Components"

ApplicationWindow {
    Material.theme: Material.Dark
    title: "RobotDeck - Test Manager"

    visible: true

    width: 1200
    height: 800

    // DarkLabel {
    //     text:"Meh ?"

    //     anchors.fill: parent
    // }

    Item {
        anchors.fill: parent

        Column {
            Label {
                 text: "meh ?"
            }

            Label {
                 text: "meh ?"
            }

            Label {
                 text: "meh ?"
            }
        }

        Button {
            anchors.centerIn: parent

            text:"Meh ?"

    //        Material.foreground: "#FFFFFF"
    //        Material.background: Material.color(Material.Grey, Material.Shade700)
        }
    }

   AssetManager {
       visible: true
   }
}
