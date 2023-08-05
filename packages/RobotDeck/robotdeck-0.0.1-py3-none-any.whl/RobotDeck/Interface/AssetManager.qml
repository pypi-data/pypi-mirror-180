/*

Copyright 2020 - 2021 Ant Solutions SRL (info@ant-solutions.be)

*/

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

Item {
    Material.theme: Material.Dark
    title: "RobotDeck - Test Manager"

    width: 640
    height: 480

    Loader {
        Image {
            id:screenImg
            anchors.fill : parent
            visible : false

            onLoaded : visible = true

            source:"http://image.intervention.io/img/intervention.svg"
        }
    }

    Item {
        id:assets

        width:150
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        ListView {
            Label {
                id:posLab

                text: "Positions"
            }

            ListView {
                id:posList

                visible:false

                anchors.top: posLab.bottom
            }

            Label {
                id:imgLab

                anchors.top: posList.bottom

                text: "Images"
            }

            ListView {
                id:imgList

                anchors.top: imgLab.bottom

                visible:false
            }

            Label {
                id:areaLab

                anchors.top: imgList.bottom

                text: "Areas"
            }


            ListView {
                id:areaList

                visible:false
            }
        }
    }

    Item {
        id:virtualScreen

        visible:screenImg.visible ? false : true

        width: pressLab.width + button.width + screenshotLab.width
        anchors.left: assets.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.right: parent.right

        Label {
            id: pressLab

            text: "Press"
        }

        Item {
            id:buttonFrame
            anchors.verticalCenter: pressLab.verticalCenter
            anchors.left: pressLab.right
            width:button.width + 30

            Button {
                id:button
                anchors.centerIn: parent

                text: "F5"

            }
        }

        Label {
            id: screenshotLab
            anchors.verticalCenter: buttonFrame.verticalCenter
            anchors.left: buttonFrame.right
            horizontalAlignment: Qt.AlignRight

            text: "to take a screenshot."
        }
    }
}
