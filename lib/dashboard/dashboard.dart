import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:alati_app/screens/roundtable_screen.dart';
import 'package:alati_app/screens/tool_inventory_screen.dart';
import 'package:alati_app/screens/reports_screen.dart';
import 'package:alati_app/screens/user_settings_screen.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  bool expanded = true;
  bool logout = false;
  int selectedTabIndex = 0;

  // Imena tabova
  List<String> tabTitles = [
    'Foam tool overview',
    'Tool Importer',
    'Report',
    'User Settings',
  ];

  // Ikone za tabove
  List<IconData> tabIcons = [
    Icons.segment_outlined,
    Icons.space_dashboard_outlined,
    Icons.calendar_today,
    Icons.settings,
  ];

  Widget _buildPlaceholderBody(BuildContext context) {
    // Tabovi koji se returnjau
    switch (selectedTabIndex) {
      case 0:
        return ToolInventoryScreen();
      case 1:
        return ToolInventoryScreen();
      case 2:
        return ReportsScreen();
      case 3:
        return Tab4();
      default:
        return Center(
            child:
                Text("Placeholder Widget for ${tabTitles[selectedTabIndex]}"));
    }
  }

//widget za foam tool ovrwier, tool importer, report, user settings kockicu
  Widget _buildTile(IconData icon, String title, int index) {
    return GestureDetector(
      onTap: () {
        setState(() {
          selectedTabIndex = index;
        });
      },
      child: Container(
        margin: EdgeInsets.symmetric(horizontal: 8, vertical: 12),
        padding: EdgeInsets.all(8),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(12),
          color: index == selectedTabIndex
              ? Colors.blue[400]!.withAlpha(100)
              : Colors.transparent,
        ),
        child: Row(children: [
          Icon(
            icon,
            color: Colors.blue[700],
          ),
          if (expanded)
            Padding(
              padding: const EdgeInsets.only(left: 16.0),
              child: Text(title),
            ),
        ]),
      ),
    );
  }

//dugme za info (pdate, koja baza, itd)
  Widget _buildInfoMenu(BuildContext context) {
    return IconButton(
      onPressed: () async {
        var version = '0.0.0'; // Placeholder verzija
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            content: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                ListTile(
                  title: Text('Jifeng Foam tool tracking app'),
                  subtitle: Text('App name'),
                ),
                ListTile(
                  title: Text(version),
                  subtitle: Text('App version'),
                ),
                ListTile(
                  title: Text(DateTime.now().toIso8601String()),
                  subtitle: Text('Application Date'),
                ),
                ListTile(
                  title: Text(
                    'Location: Database Location', // Placeholder tekst
                  ),
                  subtitle: Text('BiH'),
                ),
              ],
            ),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.maybePop(context);
                },
                child: Text('Close'),
              )
            ],
          ),
        );
      },
      icon: Icon(Icons.info_outline),
    );
  }

//dashboard koji vidimo

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Foam Tool Tracker'),
        actions: [
          _buildInfoMenu(context),
          VerticalDivider(color: Colors.white),
          IconButton(
            onPressed: () {
              setState(() {
                logout = true;
              });
              // cuva mjesto za log funkciju
              // Isto kao i predhodno
            },
            icon: logout
                ? CircularProgressIndicator(color: Colors.white)
                : Icon(Icons.logout),
          ),
        ],
      ),
      body: Stack(
        children: [
          Padding(
            padding: EdgeInsets.only(
              left: expanded ? 216 : 76,
            ),
            child: _buildPlaceholderBody(context),
          ),
          Material(
            elevation: 4,
            child: Container(
              width: expanded ? 200 : 60,
              decoration: BoxDecoration(
                border: Border(
                  right: BorderSide(color: Colors.blue[400]!, width: 1),
                ),
              ),
              child: Column(
                children: [
                  for (int index = 0; index < tabTitles.length; index++)
                    _buildTile(
                      tabIcons[index],
                      tabTitles[index],
                      index,
                    ),
                  Divider(),
                  ListTile(
                    leading: Icon(expanded
                        ? Icons.arrow_back_ios
                        : Icons.arrow_forward_ios),
                    title: Text(''),
                    onTap: () {
                      setState(() {
                        expanded = !expanded;
                      });
                    },
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

// Kod za ikone
IconData getIconForTabIndex(int index) {
  switch (index) {
    case 0:
      return Icons.segment_outlined;
    case 1:
      return Icons.space_dashboard_outlined;
    case 2:
      return Icons.calendar_month_outlined;
    case 3:
      return Icons.manage_accounts;
    default:
      return Icons.error;
  }
}
