Blender API Change Log
**********************

.. note, this document is auto generated by sphinx_changelog_gen.py


2.56 to 2.57
============
bpy.types.SplineBezierPoints
----------------------------

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.SplineBezierPoints.friction` (count), *was (number)*

bpy.types.RenderSettings
------------------------

Added
^^^^^

* :class:`bpy.types.RenderSettings.use_stamp_lens`

Removed
^^^^^^^

* **use_backbuf**

bpy.types.ActionPoseMarkers
---------------------------

Added
^^^^^

* :class:`bpy.types.ActionPoseMarkers.active`
* :class:`bpy.types.ActionPoseMarkers.active_index`

bpy.types.SpaceImageEditor
--------------------------

Renamed
^^^^^^^

* **curves** -> :class:`bpy.types.SpaceImageEditor.curve`

bpy.types.Scene
---------------

Removed
^^^^^^^

* **network_render**

bpy.types.GameObjectSettings
----------------------------

Added
^^^^^

* :class:`bpy.types.GameObjectSettings.use_material_physics_fh`

Removed
^^^^^^^

* **use_material_physics**

bpy.types.SplinePoints
----------------------

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.SplinePoints.use_material_physics` (count), *was (number)*

bpy.types.Area
--------------

Added
^^^^^

* :class:`bpy.types.Area.height`
* :class:`bpy.types.Area.width`

bpy.types.SolidifyModifier
--------------------------

Added
^^^^^

* :class:`bpy.types.SolidifyModifier.material_offset`
* :class:`bpy.types.SolidifyModifier.material_offset_rim`

Removed
^^^^^^^

* **use_rim_material**

bpy.types.UserPreferencesEdit
-----------------------------

Removed
^^^^^^^

* **use_keyframe_insert_keyingset**

bpy.types.MaterialTextureSlot
-----------------------------

Added
^^^^^

* :class:`bpy.types.MaterialTextureSlot.bump_method`
* :class:`bpy.types.MaterialTextureSlot.bump_objectspace`

Removed
^^^^^^^

* **use_old_bump**

bpy.types.ExplodeModifier
-------------------------

Added
^^^^^

* :class:`bpy.types.ExplodeModifier.particle_uv`
* :class:`bpy.types.ExplodeModifier.use_edge_cut`

Removed
^^^^^^^

* **use_edge_split**

bpy.types.Node
--------------

Added
^^^^^

* :class:`bpy.types.Node.label`

bpy.types.RigidBodyJointConstraint
----------------------------------

Added
^^^^^

* :class:`bpy.types.RigidBodyJointConstraint.limit_angle_max_x`
* :class:`bpy.types.RigidBodyJointConstraint.limit_angle_max_y`
* :class:`bpy.types.RigidBodyJointConstraint.limit_angle_max_z`
* :class:`bpy.types.RigidBodyJointConstraint.limit_angle_min_x`
* :class:`bpy.types.RigidBodyJointConstraint.limit_angle_min_y`
* :class:`bpy.types.RigidBodyJointConstraint.limit_angle_min_z`
* :class:`bpy.types.RigidBodyJointConstraint.limit_max_x`
* :class:`bpy.types.RigidBodyJointConstraint.limit_max_y`
* :class:`bpy.types.RigidBodyJointConstraint.limit_max_z`
* :class:`bpy.types.RigidBodyJointConstraint.limit_min_x`
* :class:`bpy.types.RigidBodyJointConstraint.limit_min_y`
* :class:`bpy.types.RigidBodyJointConstraint.limit_min_z`

Removed
^^^^^^^

* **limit_cone_max**
* **limit_cone_min**
* **limit_generic_max**
* **limit_generic_min**

bpy.types.KeyMap
----------------

Renamed
^^^^^^^

* **items** -> :class:`bpy.types.KeyMap.keymap_items`

bpy.types.SpaceNodeEditor
-------------------------

Added
^^^^^

* :class:`bpy.types.SpaceNodeEditor.backdrop_channels`
* :class:`bpy.types.SpaceNodeEditor.backdrop_x`
* :class:`bpy.types.SpaceNodeEditor.backdrop_y`
* :class:`bpy.types.SpaceNodeEditor.backdrop_zoom`
* :class:`bpy.types.SpaceNodeEditor.use_auto_render`

bpy.types.SPHFluidSettings
--------------------------

Added
^^^^^

* :class:`bpy.types.SPHFluidSettings.factor_density`
* :class:`bpy.types.SPHFluidSettings.factor_radius`
* :class:`bpy.types.SPHFluidSettings.factor_repulsion`
* :class:`bpy.types.SPHFluidSettings.factor_rest_length`
* :class:`bpy.types.SPHFluidSettings.factor_stiff_viscosity`
* :class:`bpy.types.SPHFluidSettings.plasticity`
* :class:`bpy.types.SPHFluidSettings.repulsion`
* :class:`bpy.types.SPHFluidSettings.spring_frames`
* :class:`bpy.types.SPHFluidSettings.stiff_viscosity`
* :class:`bpy.types.SPHFluidSettings.use_initial_rest_length`
* :class:`bpy.types.SPHFluidSettings.use_viscoelastic_springs`
* :class:`bpy.types.SPHFluidSettings.yield_ratio`

Removed
^^^^^^^

* **stiffness_near**
* **viscosity_beta**

Renamed
^^^^^^^

* **viscosity_omega** -> :class:`bpy.types.SPHFluidSettings.linear_viscosity`

bpy.types.ConstraintActuator
----------------------------

Added
^^^^^

* :class:`bpy.types.ConstraintActuator.direction_axis_pos`
* :class:`bpy.types.ConstraintActuator.fh_force`

Removed
^^^^^^^

* **spring**

bpy.types.UILayout
------------------

Renamed
^^^^^^^

* **operator_enums** -> :class:`bpy.types.UILayout.operator_enum`

bpy.types.SpaceDopeSheetEditor
------------------------------

Added
^^^^^

* :class:`bpy.types.SpaceDopeSheetEditor.show_pose_markers`

bpy.types.ToolSettings
----------------------

Added
^^^^^

* :class:`bpy.types.ToolSettings.edge_path_live_unwrap`
* :class:`bpy.types.ToolSettings.proportional_size`
* :class:`bpy.types.ToolSettings.use_keyframe_insert_keyingset`

bpy.types.EditBone
------------------

Added
^^^^^

* :class:`bpy.types.EditBone.bbone_x`
* :class:`bpy.types.EditBone.bbone_z`

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.EditBone.bbone_z` (self, matrix, scale, roll), *was (self, matrix)*

bpy.types.ID
------------

Renamed
^^^^^^^

* **update** -> :class:`bpy.types.ID.update_tag`

bpy.types.SpaceGraphEditor
--------------------------

Added
^^^^^

* :class:`bpy.types.SpaceGraphEditor.use_fancy_drawing`

bpy.types.ParticleSystem
------------------------

Added
^^^^^

* :class:`bpy.types.ParticleSystem.child_seed`

bpy.types.SpaceTimeline
-----------------------

Removed
^^^^^^^

* **use_play_3d_editors**
* **use_play_animation_editors**
* **use_play_image_editors**
* **use_play_node_editors**
* **use_play_properties_editors**
* **use_play_sequence_editors**
* **use_play_top_left_3d_editor**

bpy.types.Mesh
--------------

Added
^^^^^

* :class:`bpy.types.Mesh.validate`

Renamed
^^^^^^^

* **show_extra_edge_angle** -> :class:`bpy.types.Mesh.show_extra_face_angle`

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.Mesh.show_extra_face_angle` (self, vertices, edges, faces), *was (self, verts, edges, faces)*

bpy.types.EnumProperty
----------------------

Added
^^^^^

* :class:`bpy.types.EnumProperty.default_flag`

Renamed
^^^^^^^

* **items** -> :class:`bpy.types.EnumProperty.enum_items`

bpy.types.Screen
----------------

Added
^^^^^

* :class:`bpy.types.Screen.use_play_3d_editors`
* :class:`bpy.types.Screen.use_play_animation_editors`
* :class:`bpy.types.Screen.use_play_image_editors`
* :class:`bpy.types.Screen.use_play_node_editors`
* :class:`bpy.types.Screen.use_play_properties_editors`
* :class:`bpy.types.Screen.use_play_sequence_editors`
* :class:`bpy.types.Screen.use_play_top_left_3d_editor`

bpy.types.MirrorModifier
------------------------

Added
^^^^^

* :class:`bpy.types.MirrorModifier.use_mirror_merge`

bpy.types.Operator
------------------

Added
^^^^^

* :class:`bpy.types.Operator.cancel`

bpy.types.Brush
---------------

Added
^^^^^

* :class:`bpy.types.Brush.height`
* :class:`bpy.types.Brush.use_fixed_texture`

Renamed
^^^^^^^

* **imagepaint_tool** -> :class:`bpy.types.Brush.image_tool`
* **use_paint_texture** -> :class:`bpy.types.Brush.use_paint_image`
* **vertexpaint_tool** -> :class:`bpy.types.Brush.vertex_tool`

bpy.types.Key
-------------

Renamed
^^^^^^^

* **keys** -> :class:`bpy.types.Key.key_blocks`

bpy.types.CompositorNodeBlur
----------------------------

Added
^^^^^

* :class:`bpy.types.CompositorNodeBlur.aspect_correction`

bpy.types.SpaceTextEditor
-------------------------

Added
^^^^^

* :class:`bpy.types.SpaceTextEditor.margin_column`
* :class:`bpy.types.SpaceTextEditor.show_margin`

bpy.types.GPencilLayer
----------------------

Added
^^^^^

* :class:`bpy.types.GPencilLayer.show_x_ray`

Removed
^^^^^^^

* **active**

bpy.types.MarbleTexture
-----------------------

Renamed
^^^^^^^

* **noisebasis_2** -> :class:`bpy.types.MarbleTexture.noise_basis_2`

bpy.types.Particle
------------------

Removed
^^^^^^^

* **is_hair**

Renamed
^^^^^^^

* **keys** -> :class:`bpy.types.Particle.hair_keys`
* **keys** -> :class:`bpy.types.Particle.particle_keys`

bpy.types.Modifier
------------------

Added
^^^^^

* :class:`bpy.types.Modifier.use_apply_on_spline`

bpy.types.Property
------------------

Added
^^^^^

* :class:`bpy.types.Property.is_enum_flag`

bpy.types.SpaceProperties
-------------------------

Added
^^^^^

* :class:`bpy.types.SpaceProperties.texture_context`

Removed
^^^^^^^

* **show_brush_texture**

bpy.types.VertexGroups
----------------------

Added
^^^^^

* :class:`bpy.types.VertexGroups.remove`

Removed
^^^^^^^

* **assign**

bpy.types.Material
------------------

Added
^^^^^

* :class:`bpy.types.Material.shadow_only_type`

bpy.types.RenderLayer
---------------------

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.RenderLayer.shadow_only_type` (filename, x, y), *was (filename)*

bpy.types.Object
----------------

Added
^^^^^

* :class:`bpy.types.Object.is_modified`

Renamed
^^^^^^^

* **create_dupli_list** -> :class:`bpy.types.Object.dupli_list_create`
* **create_mesh** -> :class:`bpy.types.Object.to_mesh`
* **free_dupli_list** -> :class:`bpy.types.Object.dupli_list_clear`

bpy.types.NodeTree
------------------

Added
^^^^^

* :class:`bpy.types.NodeTree.inputs`
* :class:`bpy.types.NodeTree.outputs`

bpy.types.DopeSheet
-------------------

Added
^^^^^

* :class:`bpy.types.DopeSheet.filter_fcurve_name`
* :class:`bpy.types.DopeSheet.show_lattices`
* :class:`bpy.types.DopeSheet.show_only_matching_fcurves`

bpy.types.ActionFCurves
-----------------------

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.ActionFCurves.show_only_matching_fcurves` (data_path, index, action_group), *was (data_path, array_index, action_group)*

bpy.types.ShrinkwrapModifier
----------------------------

Added
^^^^^

* :class:`bpy.types.ShrinkwrapModifier.cull_face`

Removed
^^^^^^^

* **use_cull_back_faces**
* **use_cull_front_faces**

bpy.types.WindowManager
-----------------------

Added
^^^^^

* :class:`bpy.types.WindowManager.addon_filter`
* :class:`bpy.types.WindowManager.addon_search`
* :class:`bpy.types.WindowManager.addon_support`
* :class:`bpy.types.WindowManager.event_timer_add`
* :class:`bpy.types.WindowManager.event_timer_remove`

bpy.types.WoodTexture
---------------------

Renamed
^^^^^^^

* **noisebasis_2** -> :class:`bpy.types.WoodTexture.noise_basis_2`

bpy.types.VertexGroup
---------------------

Added
^^^^^

* :class:`bpy.types.VertexGroup.add`
* :class:`bpy.types.VertexGroup.remove`
* :class:`bpy.types.VertexGroup.weight`

bpy.types.FCurveKeyframePoints
------------------------------

Added
^^^^^

* :class:`bpy.types.FCurveKeyframePoints.insert`

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.FCurveKeyframePoints.insert` (count), *was (frame, value, replace, needed, fast)*

bpy.types.ThemeView3D
---------------------

Added
^^^^^

* :class:`bpy.types.ThemeView3D.outline_width`

bpy.types.Image
---------------

Added
^^^^^

* :class:`bpy.types.Image.pixels`

bpy.types.Bone
--------------

Added
^^^^^

* :class:`bpy.types.Bone.bbone_x`
* :class:`bpy.types.Bone.bbone_z`

bpy.types.InputKeyMapPanel
--------------------------

Removed
^^^^^^^

* **draw_entry**
* **draw_filtered**
* **draw_hierarchy**
* **draw_keymaps**
* **draw_km**
* **draw_kmi**
* **draw_kmi_properties**
* **indented_layout**

bpy.types.ParticleSettings
--------------------------

Added
^^^^^

* :class:`bpy.types.ParticleSettings.active_texture`
* :class:`bpy.types.ParticleSettings.active_texture_index`
* :class:`bpy.types.ParticleSettings.child_parting_factor`
* :class:`bpy.types.ParticleSettings.child_parting_max`
* :class:`bpy.types.ParticleSettings.child_parting_min`
* :class:`bpy.types.ParticleSettings.color_maximum`
* :class:`bpy.types.ParticleSettings.create_long_hair_children`
* :class:`bpy.types.ParticleSettings.draw_color`
* :class:`bpy.types.ParticleSettings.effector_amount`
* :class:`bpy.types.ParticleSettings.grid_random`
* :class:`bpy.types.ParticleSettings.hair_length`
* :class:`bpy.types.ParticleSettings.hexagonal_grid`
* :class:`bpy.types.ParticleSettings.is_fluid`
* :class:`bpy.types.ParticleSettings.kink_amplitude_clump`
* :class:`bpy.types.ParticleSettings.kink_flat`
* :class:`bpy.types.ParticleSettings.texture_slots`
* :class:`bpy.types.ParticleSettings.timestep`
* :class:`bpy.types.ParticleSettings.use_advanced_hair`

Removed
^^^^^^^

* **reaction_shape**
* **show_material_color**
* **use_animate_branching**
* **use_branching**
* **use_symmetric_branching**

bpy.types.SceneGameData
-----------------------

Added
^^^^^

* :class:`bpy.types.SceneGameData.show_mouse`

bpy.types.MaterialPhysics
-------------------------

Renamed
^^^^^^^

* **damping** -> :class:`bpy.types.MaterialPhysics.fh_damping`
* **distance** -> :class:`bpy.types.MaterialPhysics.fh_distance`
* **force** -> :class:`bpy.types.MaterialPhysics.fh_force`
* **use_normal_align** -> :class:`bpy.types.MaterialPhysics.use_fh_normal`


2.57 to 2.58
============

bpy_extras
----------

Added
^^^^^

* :mod:`bpy_extras`
* :mod:`bpy_extras.view3d_utils`

Moved
^^^^^

* io_utils -> :mod:`bpy_extras.io_utils`
* image_utils -> :mod:`bpy_extras.image_utils`
* mesh_utils -> :mod:`bpy_extras.mesh_utils`
* object_utils -> :mod:`bpy_extras.object_utils`

bpy.types.RenderSettings
------------------------

Added
^^^^^

* :class:`bpy.types.RenderSettings.use_bake_lores_mesh`
* :class:`bpy.types.RenderSettings.use_bake_multires`

bpy.types.Camera
----------------

Added
^^^^^

* :class:`bpy.types.Camera.show_guide`

bpy.types.SpaceImageEditor
--------------------------

Added
^^^^^

* :class:`bpy.types.SpaceImageEditor.zoom`

bpy.types.SpaceView3D
---------------------

Added
^^^^^

* :class:`bpy.types.SpaceView3D.lock_camera`

bpy.types.RegionView3D
----------------------

Added
^^^^^

* :class:`bpy.types.RegionView3D.is_perspective`

bpy.types.Scene
---------------

Added
^^^^^

* :class:`bpy.types.Scene.frame_subframe`

bpy.types.Area
--------------

Removed
^^^^^^^

* **active_space**

bpy.types.DisplaceModifier
--------------------------

Renamed
^^^^^^^

* **texture_coordinate_object** -> :class:`bpy.types.DisplaceModifier.texture_coords_object`

bpy.types.UserPreferencesView
-----------------------------

Added
^^^^^

* :class:`bpy.types.UserPreferencesView.use_camera_lock_parent`

bpy.types.DomainFluidSettings
-----------------------------

Added
^^^^^

* :class:`bpy.types.DomainFluidSettings.fluid_mesh_vertices`
* :class:`bpy.types.DomainFluidSettings.surface_noobs`

bpy.types.Sculpt
----------------

Added
^^^^^

* :class:`bpy.types.Sculpt.use_deform_only`

bpy.types.ClothCollisionSettings
--------------------------------

Added
^^^^^

* :class:`bpy.types.ClothCollisionSettings.distance_repel`
* :class:`bpy.types.ClothCollisionSettings.repel_force`

bpy.types.UILayout
------------------

Added
^^^^^

* :class:`bpy.types.UILayout.template_edit_mode_selection`

bpy.types.ToolSettings
----------------------

Added
^^^^^

* :class:`bpy.types.ToolSettings.use_snap_project_self`

bpy.types.Mesh
--------------

Removed
^^^^^^^

* **edge_face_count**
* **edge_face_count_dict**
* **edge_loops_from_edges**
* **edge_loops_from_faces**

bpy.types.PointDensity
----------------------

Added
^^^^^

* :class:`bpy.types.PointDensity.falloff_curve`
* :class:`bpy.types.PointDensity.falloff_speed_scale`
* :class:`bpy.types.PointDensity.use_falloff_curve`

bpy.types.SpaceTextEditor
-------------------------

Added
^^^^^

* :class:`bpy.types.SpaceTextEditor.use_match_case`

bpy.types.CameraActuator
------------------------

Added
^^^^^

* :class:`bpy.types.CameraActuator.damping`

bpy.types.Property
------------------

Added
^^^^^

* :class:`bpy.types.Property.is_skip_save`

bpy.types.UserPreferencesSystem
-------------------------------

Added
^^^^^

* :class:`bpy.types.UserPreferencesSystem.anisotropic_filter`

bpy.types.Object
----------------

Added
^^^^^

* :class:`bpy.types.Object.empty_image_offset`

bpy.types.Image
---------------

Added
^^^^^

* :class:`bpy.types.Image.resolution`

bpy.types.SceneGameData
-----------------------

Added
^^^^^

* :class:`bpy.types.SceneGameData.use_glsl_color_management`


2.58 to 2.59
============

bpy.types.Scene
---------------

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.Scene.collada_export` (filepath, selected), *was (filepath)*

bpy.types.MultiresModifier
--------------------------

Added
^^^^^

* :class:`bpy.types.MultiresModifier.use_subsurf_uv`

bpy.types.KeyMap
----------------

Removed
^^^^^^^

* **copy_to_user**

Renamed
^^^^^^^

* **is_user_defined** -> :class:`bpy.types.KeyMap.is_user_modified`

bpy.types.SceneRenderLayer
--------------------------

Added
^^^^^

* :class:`bpy.types.SceneRenderLayer.use_pass_material_index`

bpy.types.ToolSettings
----------------------

Renamed
^^^^^^^

* **use_snap_project_self** -> :class:`bpy.types.ToolSettings.use_snap_self`

bpy.types.UserPreferencesInput
------------------------------

Added
^^^^^

* :class:`bpy.types.UserPreferencesInput.ndof_fly_helicopter`
* :class:`bpy.types.UserPreferencesInput.ndof_lock_horizon`
* :class:`bpy.types.UserPreferencesInput.ndof_orbit_invert_axes`
* :class:`bpy.types.UserPreferencesInput.ndof_sensitivity`
* :class:`bpy.types.UserPreferencesInput.ndof_show_guide`
* :class:`bpy.types.UserPreferencesInput.ndof_zoom_invert`
* :class:`bpy.types.UserPreferencesInput.ndof_zoom_updown`

Removed
^^^^^^^

* **edited_keymaps**
* **ndof_pan_speed**
* **ndof_rotate_speed**

bpy.types.IDMaterials
---------------------

Function Arguments
^^^^^^^^^^^^^^^^^^

* :class:`bpy.types.IDMaterials.pop` (index, update_data), *was (index)*

bpy.types.Material
------------------

Added
^^^^^

* :class:`bpy.types.Material.pass_index`

bpy.types.RenderLayer
---------------------

Added
^^^^^

* :class:`bpy.types.RenderLayer.use_pass_material_index`

bpy.types.Object
----------------

Added
^^^^^

* :class:`bpy.types.Object.closest_point_on_mesh`

bpy.types.ThemeNodeEditor
-------------------------

Added
^^^^^

* :class:`bpy.types.ThemeNodeEditor.noodle_curving`

bpy.types.ChildOfConstraint
---------------------------

Added
^^^^^

* :class:`bpy.types.ChildOfConstraint.inverse_matrix`

bpy.types.KeyConfigurations
---------------------------

Added
^^^^^

* :class:`bpy.types.KeyConfigurations.addon`
* :class:`bpy.types.KeyConfigurations.user`

bpy.types.Image
---------------

Added
^^^^^

* :class:`bpy.types.Image.use_generated_float`

bpy.types.KeyMapItem
--------------------

Added
^^^^^

* :class:`bpy.types.KeyMapItem.is_user_modified`


2.59 to 2.60
============

.. These have been manually added wait until RC to do final changelog!

bpy.types.MeshTextureFace
-------------------------

Removed
^^^^^^^

* **use_image**
* **use_object_color**
* **use_blend_shared**

Moved
^^^^^

* **hide** -> :class:`bpy.types.Material.game_settings.invisible`
* **use_collision** -> :class:`bpy.types.Material.game_settings.physics`
* **use_light** -> :class:`bpy.types.Material.game_settings.use_shadeless`
* **use_twoside** -> :class:`bpy.types.Material.game_settings.backface_culling`
* **use_bitmap_text** -> :class:`bpy.types.Material.game_settings.text`
* **blend_type** -> :class:`bpy.types.Material.game_settings.alpha_blend`
* **use_alpha_sort** -> :class:`bpy.types.Material.game_settings.alpha_blend`
* **use_billboard** -> :class:`bpy.types.Material.game_settings.face_orientation`
* **use_halo** -> :class:`bpy.types.Material.game_settings.face_orientation`
* **use_shadow_cast** -> :class:`bpy.types.Material.game_settings.face_orientation`

.. Automatically Generated, 2.59 -> r40804!

bpy.types.RenderSettings
------------------------

Added
^^^^^

* :class:`bpy.types.RenderSettings.ffmpeg_audio_channels`

bpy.types.DriverTarget
----------------------

Added
^^^^^

* :class:`bpy.types.DriverTarget.transform_space`

Removed
^^^^^^^

* **use_local_space_transform**

bpy.types.Sound
---------------

Added
^^^^^

* :class:`bpy.types.Sound.factory`
* :class:`bpy.types.Sound.use_mono`

bpy.types.Camera
----------------

Added
^^^^^

* :class:`bpy.types.Camera.view_frame`

bpy.types.Scene
---------------

Added
^^^^^

* :class:`bpy.types.Scene.audio_volume`

bpy.types.KeyingSet
-------------------

Added
^^^^^

* :class:`bpy.types.KeyingSet.refresh`

bpy.types.Armature
------------------

Added
^^^^^

* :class:`bpy.types.Armature.deform_method`

bpy.types.GameObjectSettings
----------------------------

Added
^^^^^

* :class:`bpy.types.GameObjectSettings.obstacle_radius`
* :class:`bpy.types.GameObjectSettings.use_obstacle_create`

bpy.types.BlendData
-------------------

Added
^^^^^

* :class:`bpy.types.BlendData.speakers`

bpy.types.SolidifyModifier
--------------------------

Added
^^^^^

* :class:`bpy.types.SolidifyModifier.thickness_vertex_group`

bpy.types.ThemeGraphEditor
--------------------------

Added
^^^^^

* :class:`bpy.types.ThemeGraphEditor.handle_auto_clamped`
* :class:`bpy.types.ThemeGraphEditor.handle_sel_auto_clamped`

bpy.types.CompositorNodeIDMask
------------------------------

Added
^^^^^

* :class:`bpy.types.CompositorNodeIDMask.use_smooth_mask`

bpy.types.Node
--------------

Added
^^^^^

* :class:`bpy.types.Node.parent`

bpy.types.Texture
-----------------

Added
^^^^^

* :class:`bpy.types.Texture.evaluate`

bpy.types.UILayout
------------------

Added
^^^^^

* :class:`bpy.types.UILayout.template_keymap_item_properties`

bpy.types.ToolSettings
----------------------

Added
^^^^^

* :class:`bpy.types.ToolSettings.use_multipaint`

bpy.types.UserPreferencesInput
------------------------------

Added
^^^^^

* :class:`bpy.types.UserPreferencesInput.ndof_panx_invert_axis`
* :class:`bpy.types.UserPreferencesInput.ndof_pany_invert_axis`
* :class:`bpy.types.UserPreferencesInput.ndof_panz_invert_axis`
* :class:`bpy.types.UserPreferencesInput.ndof_roll_invert_axis`
* :class:`bpy.types.UserPreferencesInput.ndof_rotate_invert_axis`
* :class:`bpy.types.UserPreferencesInput.ndof_tilt_invert_axis`

bpy.types.LockedTrackConstraint
-------------------------------

Added
^^^^^

* :class:`bpy.types.LockedTrackConstraint.head_tail`

bpy.types.SpaceGraphEditor
--------------------------

Moved
^^^^^

* use_fancy_drawing -> :class:`bpy.types.SpaceGraphEditor.use_beauty_drawing`

bpy.types.ParticleSystem
------------------------

Added
^^^^^

* :class:`bpy.types.ParticleSystem.dt_frac`

bpy.types.Mesh
--------------

Added
^^^^^

* :class:`bpy.types.Mesh.use_paint_mask_vertex`

bpy.types.FCurve
----------------

Removed
^^^^^^^

* **use_auto_handle_clamp**

bpy.types.DampedTrackConstraint
-------------------------------

Added
^^^^^

* :class:`bpy.types.DampedTrackConstraint.head_tail`

bpy.types.ImageTexture
----------------------

Added
^^^^^

* :class:`bpy.types.ImageTexture.use_derivative_map`

bpy.types.SoundSequence
-----------------------

Added
^^^^^

* :class:`bpy.types.SoundSequence.pan`
* :class:`bpy.types.SoundSequence.pitch`

Removed
^^^^^^^

* **attenuation**

bpy.types.FModifier
-------------------

Added
^^^^^

* :class:`bpy.types.FModifier.blend_in`
* :class:`bpy.types.FModifier.blend_out`
* :class:`bpy.types.FModifier.frame_end`
* :class:`bpy.types.FModifier.frame_start`
* :class:`bpy.types.FModifier.influence`
* :class:`bpy.types.FModifier.use_influence`
* :class:`bpy.types.FModifier.use_restricted_range`

bpy.types.EnvironmentMap
------------------------

Added
^^^^^

* :class:`bpy.types.EnvironmentMap.clear`
* :class:`bpy.types.EnvironmentMap.is_valid`
* :class:`bpy.types.EnvironmentMap.save`

bpy.types.UserPreferencesSystem
-------------------------------

Added
^^^^^

* :class:`bpy.types.UserPreferencesSystem.use_translate_interface`

Removed
^^^^^^^

* **use_translate_buttons**
* **use_translate_toolbox**

bpy.types.LimitDistanceConstraint
---------------------------------

Added
^^^^^

* :class:`bpy.types.LimitDistanceConstraint.head_tail`
* :class:`bpy.types.LimitDistanceConstraint.use_transform_limit`

bpy.types.MovieSequence
-----------------------

Added
^^^^^

* :class:`bpy.types.MovieSequence.stream_index`

bpy.types.Material
------------------

Added
^^^^^

* :class:`bpy.types.Material.game_settings`

bpy.types.Object
----------------

Added
^^^^^

* :class:`bpy.types.Object.matrix_parent_inverse`

bpy.types.SequenceProxy
-----------------------

Added
^^^^^

* :class:`bpy.types.SequenceProxy.build_100`
* :class:`bpy.types.SequenceProxy.build_25`
* :class:`bpy.types.SequenceProxy.build_50`
* :class:`bpy.types.SequenceProxy.build_75`
* :class:`bpy.types.SequenceProxy.build_free_run`
* :class:`bpy.types.SequenceProxy.build_free_run_rec_date`
* :class:`bpy.types.SequenceProxy.build_record_run`
* :class:`bpy.types.SequenceProxy.quality`
* :class:`bpy.types.SequenceProxy.timecode`

bpy.types.Sequence
------------------

Added
^^^^^

* :class:`bpy.types.Sequence.waveform`

bpy.types.DopeSheet
-------------------

Added
^^^^^

* :class:`bpy.types.DopeSheet.show_datablock_filters`
* :class:`bpy.types.DopeSheet.show_speakers`

bpy.types.ActionActuator
------------------------

Added
^^^^^

* :class:`bpy.types.ActionActuator.apply_to_children`
* :class:`bpy.types.ActionActuator.layer`
* :class:`bpy.types.ActionActuator.layer_weight`
* :class:`bpy.types.ActionActuator.use_additive`
* :class:`bpy.types.ActionActuator.use_force`
* :class:`bpy.types.ActionActuator.use_local`

bpy.types.VertexGroup
---------------------

Added
^^^^^

* :class:`bpy.types.VertexGroup.lock_weight`

bpy.types.ThemeView3D
---------------------

Added
^^^^^

* :class:`bpy.types.ThemeView3D.speaker`

bpy.types.Image
---------------

Added
^^^^^

* :class:`bpy.types.Image.pack`
* :class:`bpy.types.Image.unpack`

bpy.types.Curve
---------------

Added
^^^^^

* :class:`bpy.types.Curve.fill_mode`

Removed
^^^^^^^

* **use_fill_back**
* **use_fill_front**

bpy.types.ParticleSettings
--------------------------

Added
^^^^^

* :class:`bpy.types.ParticleSettings.adaptive_subframes`
* :class:`bpy.types.ParticleSettings.courant_target`

bpy.types.SceneGameData
-----------------------

Added
^^^^^

* :class:`bpy.types.SceneGameData.level_height`
* :class:`bpy.types.SceneGameData.obstacle_simulation`
* :class:`bpy.types.SceneGameData.recast_data`
* :class:`bpy.types.SceneGameData.restrict_animation_updates`
* :class:`bpy.types.SceneGameData.show_obstacle_simulation`

