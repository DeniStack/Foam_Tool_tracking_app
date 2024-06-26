// maintenance_cubit.dart
import 'package:flutter_bloc/flutter_bloc.dart';
import '/models/tool_model.dart';

class MaintenanceCubit extends Cubit<List<Tool>> {
  MaintenanceCubit() : super([]);

  void updateTools(List<Tool> newTools) {
    emit(newTools);
  }

  void addTool(Tool tool) {
    state.add(tool);
    emit(List.from(state));
  }

  void removeTool(String toolName) {
    state.removeWhere((tool) => tool.name == toolName);
    emit(List.from(state));
  }
}